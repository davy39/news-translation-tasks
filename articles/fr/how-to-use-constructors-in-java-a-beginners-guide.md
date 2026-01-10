---
title: 'Comment utiliser les constructeurs en Java : Un guide pour débutants'
subtitle: ''
author: Ateev Duggal
co_authors: []
series: null
date: '2025-07-08T18:15:32.094Z'
originalURL: https://freecodecamp.org/news/how-to-use-constructors-in-java-a-beginners-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751998519087/7808c004-c8e5-4e63-b293-10fa479a179f.png
tags:
- name: Java
  slug: java
- name: Beginner Developers
  slug: beginners
- name: constructors
  slug: constructors
seo_title: 'Comment utiliser les constructeurs en Java : Un guide pour débutants'
seo_desc: Java is an object-oriented programming language that is centred around the
  concept of objects. Objects are like real-world entities that are created with the
  new keyword and occupy memory. But all this happens in the front-end code – so what
  about th...
---

Java est un langage de programmation orienté objet qui est centré autour du concept d'objets. Les objets sont comme des entités du monde réel qui sont créées avec le mot-clé new et occupent de la mémoire. Mais tout cela se passe dans le code front-end – alors qu'en est-il du back-end ? Comment les objets sont-ils créés et initialisés avec des valeurs ?

C'est là que les constructeurs entrent en jeu. Les constructeurs sont des types spéciaux de méthodes sans type de retour. Ils sont principalement utilisés pour initialiser l'objet, pour configurer son état interne, ou pour attribuer des valeurs par défaut à ses attributs.

Dans ce tutoriel, nous allons approfondir le sujet des constructeurs en Java. Vous apprendrez comment ils fonctionnent et pourquoi ils sont essentiels dans la création d'objets et la programmation Java. À la fin, j'espère que vous comprendrez pourquoi ils sont l'un des concepts fondamentaux de la POO.

Commençons...

### Prérequis

Vous n'avez pas besoin de connaître des concepts trop avancés pour commencer à apprendre les constructeurs en Java. Une compréhension de base de la syntaxe Java, des classes, des objets, des méthodes, des paramètres, des arguments et des modificateurs d'accès est suffisante pour commencer.

## Ce que nous allons couvrir :

* [Qu'est-ce que les constructeurs en Java ?](#heading-qu-est-ce-que-les-constructeurs-en-java)
    
    * [Syntaxe du constructeur :](#heading-syntaxe-du-constructeur)
        
* [Types de constructeurs](#heading-types-de-constructeurs)
    
    * [Constructeur par défaut](#heading-constructeur-par-defaut)
        
    * [Constructeur sans argument](#heading-constructeur-sans-argument)
        
    * [Constructeur paramétré](#heading-constructeur-parametre)
        
    * [Constructeur de copie](#heading-constructeur-de-copie)
        
* [Que se passe-t-il en coulisses lorsqu'un constructeur est appelé en Java ?](#heading-que-se-passe-t-il-en-coulisses-lorsqu-un-constructeur-est-appel-en-java)
    
* [Comment utiliser le mot-clé return dans les constructeurs](#heading-comment-utiliser-le-mot-cle-return-dans-les-constructeurs)
    
    * [Code d'exemple :](#heading-code-d-exemple)
        
    * [Exemple :](#heading-exemple-4)
        
* [Conclusion](#heading-conclusion)
    
* [Questions fréquemment posées](#heading-questions-frequemment-posees)
    

## **Qu'est-ce que les constructeurs en Java ?**

Comme mentionné ci-dessus, les constructeurs sont des types spéciaux de méthodes qui :

1. n'ont pas de type de retour (pas même void),
    
2. ont le même nom que la classe
    
3. sont appelés automatiquement lorsqu'un objet est créé en utilisant le mot-clé new.
    

Le but principal d'un constructeur est d'initialiser un nouvel objet, de configurer son état interne, ou d'attribuer des valeurs par défaut à ses attributs.

Les constructeurs peuvent également être compris comme un bloc spécial de code qui est appelé lorsqu'un objet est créé – soit automatiquement, soit manuellement en le codant en dur – avec les valeurs que nous voulons utiliser pour initialiser l'objet.

Si nous sommes d'accord pour que l'objet utilise des valeurs par défaut (comme 0 pour les nombres ou null pour les objets), Java le gérera pour nous automatiquement. Mais si nous voulons donner à l'objet des valeurs spécifiques lors de sa création, nous devons écrire un constructeur qui prend ces valeurs comme paramètres et les utilise pour configurer l'objet.

### **Syntaxe du constructeur :**

```java
class NomDeClasse {

    // Constructeur par défaut avec modificateur d'accès
    [modificateur_d'accès] NomDeClasse(paramètres...) {
        // corps du constructeur
    }

}
```

### Exemples

**Lorsque le constructeur n'est pas défini explicitement**

```java
class Voiture {

    String marque;
    int année;

    // Aucun constructeur n'est défini, donc Java en fournit un par défaut
}

public class Main {

    public static void main(String[] args) {

        Voiture voiture1 = new Voiture();  // Java appelle le constructeur par défaut

        // Valeurs par défaut : marque = null, année = 0
        System.out.println("Marque : " + voiture1.marque);
        System.out.println("Année : " + voiture1.année);
    }
}
```

Sortie :

![sortie du code dans lequel il n'y a pas de constructeur](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcTW6FYYmq8kB1QL_vSBNqbaVBgo7hLXvqmA3l52HBh9Yvq4AN1aLIAKRqqiOz_tDcCFOTWBVoO1bgjWOD2yyt1nykuobAPQTWRayjqK0jDu2COmPxqI5AaapIyFzDbkrvreV-qyw?key=-LGNq3k7xufJJBHkVFXMZw align="center")

Dans le code ci-dessus, nous avons une classe **Voiture** avec deux variables :

1. marque de type `String`
    
2. année de type `int`
    

Puisqu'une classe n'est qu'un plan, nous devons créer un objet pour l'utiliser réellement. Cela est fait dans la classe `Main`. Lorsque nous créons un objet Voiture en utilisant `new` Voiture(), Java recherche un constructeur. Parce que nous n'en avons pas défini un, le compilateur fournit automatiquement un constructeur par défaut (un sans arguments).

Cela nous permet de créer l'objet et d'imprimer ses variables sans aucune erreur. Les valeurs imprimées seront les valeurs par défaut — `null` **pour le** `String`**, et** `0` **pour le** `int`**.**

Nous approfondirons comment cela fonctionne en coulisses plus tard, étape par étape, pour que ce soit plus facile à comprendre.

**Lorsque nous avons défini un constructeur**

```java
public class Voiture {

    String marque;
    int année;

    // Constructeur avec paramètres pour initialiser des valeurs personnalisées
    public Voiture(String nomMarque, int annéeModèle) {
        marque = nomMarque;
        année = annéeModèle;
    }
}

public class Main {

    public static void main(String[] args) {

        Voiture voiture2 = new Voiture("Toyota", 2022);  // Valeurs personnalisées

        System.out.println("Marque : " + voiture2.marque);
        System.out.println("Année : " + voiture2.année);
    }
}
```

**Sortie**

![Sortie du code qui a un constructeur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751864448284/2cbb8360-1c6d-42b8-811f-b7603625288d.png align="center")

Il s'agit du même code que précédemment, avec une différence clé : cette fois, nous avons explicitement défini un constructeur. Grâce à cela, la sortie que nous voyons n'est pas les valeurs par défaut (`null` pour `String`, `0` pour `int`), mais les valeurs personnalisées que nous avons fournies.

Comment cela se produit-il ? Simple – nous passons des valeurs comme arguments lors de la création de l'objet :

`Voiture voiture2 = new Voiture("Toyota", 2022);`

Ces valeurs sont reçues par le constructeur comme paramètres et sont ensuite utilisées pour initialiser les variables de l'objet. En conséquence, au lieu des valeurs par défaut, nous obtenons la marque et l'année que nous avons spécifiées.

## **Types de constructeurs**

Il existe principalement quatre types de constructeurs :

1. Constructeurs par défaut
    
2. Constructeur sans arguments
    
3. Constructeur paramétré
    
4. Constructeur de copie
    

![Types de constructeurs](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfafO5dDmX5UA0ADQI5Q8DZSU2H_bVlHjmtKdDpMkmWB4Rhui1kR4w_BP_7-mPz6eb9KdGkVmYxYsZHa4HI044mz3O0CXtXJZBhpJr_wCqWgLO6U0BDUNzm_C9piUHfyXr84xEsoQ?key=-LGNq3k7xufJJBHkVFXMZw align="center")

### **Constructeur par défaut**

Un type de constructeur sans argument qui est ajouté par le compilateur lors du processus de compilation afin que les valeurs de l'objet puissent être initialisées. Il n'est ajouté par le compilateur que si vous n'en ajoutez pas un explicitement.

#### **Syntaxe :**

```java
public class MaClasse {

    public MaClasse() {
        // Corps du constructeur
    }

}
```

#### **Exemple**

```java
public class Vélo {

    // Aucun constructeur défini ici
    // Le compilateur ajoutera automatiquement un constructeur par défaut

    public static void main(String[] args) {
        Vélo monVélo = new Vélo();  // Appelle le constructeur par défaut fourni par le compilateur
        System.out.println("Objet Vélo créé !");
    }

}
```

Le code devient le suivant après que le compilateur a ajouté un constructeur par défaut lors du processus de compilation :

```java
public class Vélo {

    // Constructeur par défaut ajouté par le compilateur
    public Vélo() {
        super();  // Appelle le constructeur de la classe Object
    }

    public static void main(String[] args) {
        Vélo monVélo = new Vélo();  // Appelle maintenant ce constructeur par défaut explicite
        System.out.println("Objet Vélo créé !");
    }

}
```

#### **Sortie**

Objet Vélo créé !

![Constructeur par défaut](https://cdn.hashnode.com/res/hashnode/image/upload/v1751867033814/3296a90c-3576-4a57-a863-fe0d1acfafa2.png align="center")

### **Constructeur sans argument**

Le constructeur sans argument est un type de constructeur que vous écrivez explicitement dans votre code et qui ne contient aucun paramètre.

Maintenant, vous vous demandez peut-être... N'est-ce pas la même chose que le constructeur par défaut ? La réponse est à la fois oui et non.

Il n'y a pas beaucoup de différence entre le constructeur par défaut et le constructeur sans argument, car tous deux ne prennent aucun paramètre. Mais il y a une différence clé.

Le constructeur par défaut, comme nous l'avons déjà discuté, est un type de constructeur sans argument qui est automatiquement ajouté par le compilateur lorsqu'il n'en trouve pas dans notre code. En revanche, un constructeur sans argument est un type de constructeur que nous écrivons dans notre code.

En bref, si le compilateur est celui qui ajoute un constructeur lors du processus de compilation, il est appelé constructeur par défaut. Mais si nous sommes ceux qui ajoutons le constructeur, il est appelé constructeur sans argument.

La principale différence entre un constructeur par défaut et un constructeur défini par l'utilisateur est **comment ils sont créés et ce qu'ils font**.

* Un **constructeur par défaut** est automatiquement ajouté par le compilateur **si nous n'en ajoutons pas un nous-mêmes**. Il ne fait pas grand-chose – il appelle simplement la classe parente (généralement la `classe Object`) et définit toutes les variables à leurs valeurs par défaut. Par exemple, `int` devient `0` et les objets deviennent `null`.
    
* Un **constructeur défini par l'utilisateur** est celui que **nous écrivons nous-mêmes**. Nous pouvons ajouter une logique personnalisée à l'intérieur, définir des valeurs personnalisées aux variables, et utiliser des modificateurs d'accès comme `public`, `private`, ou `protected`. Cela signifie que nous pouvons décider comment l'objet doit être configuré lorsqu'il est créé.
    

Notez que même si nous n'écrivons pas `super()` dans notre constructeur, Java l'ajoute automatiquement à moins que nous n'appelions un autre constructeur avec `this()` ou que nous n'appelions un `super(...)` différent avec des paramètres.

Nous comprendrons cela en profondeur dans la section suivante.

| **Aspect** | **Constructeur par défaut** | **Constructeur sans argument** |
| --- | --- | --- |
| **Définition** | Un constructeur est automatiquement fourni par le compilateur lorsqu'aucun autre constructeur n'existe. | Un constructeur explicitement écrit par le programmeur qui ne prend aucun argument. |
| **Définis par** | Compilateur | Programmeur |
| **Logique personnalisée** | Non possible – ne fait que l'initialisation de base par défaut | Oui – peut contenir toute logique d'initialisation |
| **Quand disponible** | Seulement si la classe n'a aucun constructeur défini du tout | Lorsqu'il est explicitement écrit par le programmeur |
| **But** | Permettre la création d'objets avec une initialisation par défaut | Permettre la création d'objets avec un comportement défini par le programmeur |

#### **Syntaxe :**

```java
class NomDeClasse {

    public NomDeClasse() {
        // Corps (facultatif)
    }

}
```

#### **Exemple**

Utilisons le même exemple de Vélo que nous avons utilisé pour expliquer le constructeur par défaut.

```java
public class Vélo {

    public Vélo() {
        System.out.println("Objet Vélo créé !");
    }

    public static void main(String[] args) {
        Vélo monVélo = new Vélo();
    }
}
```

#### **Sortie :**

Objet Vélo créé !

![Constructeur sans argument](https://cdn.hashnode.com/res/hashnode/image/upload/v1751868234945/565ec06d-7e4d-4415-b983-f517c721d0b9.png align="center")

Dans le code ci-dessus, nous avons défini un constructeur dans notre code lors de son écriture. Cela signifie que c'est un exemple de constructeur sans argument.

Nous savons que les deux types de constructeurs sont définis sans aucun paramètre, mais qu'en est-il du corps ? Nous n'avons rien dit à ce sujet. Voyons ce qui se passe si nous écrivons du code avec un constructeur sans argument sans corps :

```java
public class Vélo {

    Vélo() {
        // Pas de corps
    }

    public static void main(String[] args) {
        Vélo monVélo = new Vélo(); // Appelle le constructeur sans argument défini par l'utilisateur
        System.out.println("Objet Vélo créé !");
    }
}
```

#### **Sortie :**

Objet Vélo créé !

Le code est toujours compilé car le compilateur ajoute le mot-clé `super()` lors du processus de compilation, qui initialise l'objet en utilisant la classe objet.

### **Constructeur paramétré**

Un constructeur qui accepte des paramètres est appelé constructeur paramétré et n'est utilisé que lorsque nous devons initialiser les attributs d'un objet avec des valeurs personnalisées.

* Paramètre fait référence à la variable listée dans la définition du constructeur ou de la méthode.
    
* Argument est la valeur réelle passée lors de l'appel du constructeur ou de la méthode.
    

Il nous donne la flexibilité d'initialiser notre objet avec des valeurs personnalisées données au moment de la création de l'objet.

#### **Syntaxe**

Voici la syntaxe pour un constructeur paramétré qui prend un paramètre :

```java
class NomDeClasse {

    // Membres de données (variables d'instance)
    TypeDeDonnée variable1;

    // Constructeur paramétré
    NomDeClasse(TypeDeDonnée param1) {
        variable1 = param1;
    }

    // Méthode principale pour créer des objets
    public static void main(String[] args) {
        // Création d'objet en utilisant le constructeur paramétré
        NomDeClasse obj = new NomDeClasse(valeur1);
    }
}
```

#### **Exemple**

Nous allons à nouveau utiliser l'exemple de Vélo pour cela.

```java
public class Vélo {

    String nomModèle;  // variable d'instance

    // Constructeur paramétré
    Vélo(String modèle) {
        nomModèle = modèle;
    }

    public static void main(String[] args) {
        // Passer le paramètre lors de la création de l'objet Vélo
        Vélo monVélo = new Vélo("Vélo de montagne");
        System.out.println("Objet Vélo créé ! Modèle : " + monVélo.nomModèle);
    }
}
```

#### Sortie :

Objet Vélo créé ! Modèle : Vélo de montagne

![Constructeur paramétré](https://cdn.hashnode.com/res/hashnode/image/upload/v1751870395133/72bcbe0c-3a7c-4cc1-87d4-1ae9106b21d9.png align="center")

Dans cet exemple, nous travaillons avec une classe Vélo qui a une variable d'instance de type de données String appelée nomModèle, et un constructeur pour définir la valeur de cette variable.

Le constructeur prend un paramètre appelé modèle et l'assigne à nomModèle. Ainsi, lorsque nous créons un nouvel objet Vélo et passons la chaîne "Vélo de montagne", le constructeur stocke cette valeur dans la variable nomModèle.

Grâce à cela, lorsque nous imprimons le nom du modèle, nous voyons "Vélo de montagne" au lieu de null, qui est la valeur par défaut du type de données String, car la valeur de nomModèle a été mise à jour.

### **Constructeur de copie**

Un constructeur de copie est utilisé pour créer un nouvel objet comme une copie de l'objet existant. Contrairement au C++, Java n'a pas de constructeur de copie par défaut. Au lieu de cela, nous devons créer le nôtre en créant un constructeur qui prend un objet de la même classe comme paramètre et copie ses champs.

#### **Syntaxe**

```java
class NomDeClasse {

    // Champs
    TypeDeDonnée1 champ1;
    TypeDeDonnée2 champ2;
    // ... autres champs

    // Constructeur normal
    NomDeClasse(TypeDeDonnée1 f1, TypeDeDonnée2 f2) {
        champ1 = f1;
        champ2 = f2;
        // ... initialiser d'autres champs
    }

    // Constructeur de copie 
    NomDeClasse(NomDeClasse autre) {
        champ1 = autre.champ1;
        champ2 = autre.champ2;
        // ... copier d'autres champs
    }
}
```

#### **Exemple**

```java
public class Vélo {

    String nomModèle;  // variable d'instance

    // Constructeur paramétré
    Vélo(String modèle) {
        nomModèle = modèle;
    }

    // Constructeur de copie
    Vélo(Vélo autreVélo) {
        nomModèle = autreVélo.nomModèle;
    }

    public static void main(String[] args) {
        // Créer un objet Vélo en utilisant le constructeur paramétré
        Vélo monVélo = new Vélo("Vélo de montagne");
        System.out.println("Objet Vélo créé ! Modèle : " + monVélo.nomModèle);

        // Créer une copie de l'objet Vélo existant en utilisant le constructeur de copie
        Vélo véloCopié = new Vélo(monVélo);
        System.out.println("Objet Vélo copié créé ! Modèle : " + véloCopié.nomModèle);
    }
}
```

#### **Sortie :**

Objet Vélo créé ! Modèle : Vélo de montagne

Objet Vélo copié créé ! Modèle : Vélo de montagne

![Constructeur de copie](https://cdn.hashnode.com/res/hashnode/image/upload/v1751874707838/772bdc8a-75d7-437d-a296-7f472fe5c764.png align="center")

Dans le code ci-dessus, nous avons créé un constructeur de copie pour copier les valeurs de l'objet (monVélo) dans un nouvel objet (véloCopié), que nous avons défini dans la classe principale.

Mais la manière dont le nouvel objet est appelé est un peu différente. Au lieu de passer des arguments pour le constructeur, nous avons passé l'objet original.

#### **Pourquoi les constructeurs de copie ?**

Un constructeur de copie est utilisé pour faire une copie de l'objet, mais vous pouvez également faire une copie en utilisant la méthode clone() ou la méthode object.clone(). Alors pourquoi utilisons-nous un constructeur de copie ?

Le constructeur de copie fait une copie profonde, tandis que la méthode clone fait une copie superficielle de l'objet. Il y a diverses choses que vous devez savoir avant d'utiliser des techniques de clonage, comme [CloneNotSupportedException](https://docs.oracle.com/javase/8/docs/api/java/lang/CloneNotSupportedException.html)**.**

D'autre part, les constructeurs de copie sont clairs et faciles à comprendre, et fonctionnent bien avec les champs finaux. Nous pouvons contrôler comment la copie se fait (profonde vs superficielle) et surtout lorsque nous traitons avec des objets mutables.

## **Que se passe-t-il en coulisses lorsqu'un constructeur est appelé en Java ?**

Donc, pour résumer : lorsque nous créons un objet en utilisant le mot-clé `new`, un constructeur est automatiquement appelé. Si nous n'avons défini aucun constructeur dans notre classe, Java définit automatiquement un constructeur pour nous.

Mais lors de l'écriture et de l'exécution de notre code, nous nous concentrons principalement sur ce qui est visible dans notre éditeur, c'est-à-dire ce que nous pouvons voir. Plongeons un peu plus profondément et explorons ce qui se passe en coulisses – au niveau du compilateur et de la JVM – lorsqu'un objet est créé et exécuté.

* **Étape 1 : Allocation de mémoire** – Lorsque nous créons un objet en utilisant un nouveau mot-clé, Java alloue de la mémoire pour cet objet dans le tas. Cette mémoire est l'endroit où les champs de l'objet (également appelés attributs) seront placés.
    
* **Étape 2 : Création de référence** – Une référence à cet objet est stockée sur la pile, ce qui permet à notre programme d'interagir avec l'objet qui vit dans le tas.
    
* **Étape 3 : Création du constructeur** – Java détermine ensuite quel constructeur appeler. Si aucun constructeur n'est explicitement défini dans notre classe, le compilateur insère automatiquement un constructeur sans paramètres.
    
* **Étape 4 : Appel du constructeur de la superclasse** – Avant d'exécuter le corps du constructeur, Java appelle d'abord le constructeur de la superclasse en utilisant le mot-clé `super()`. Cela garantit que les champs hérités de la classe parente sont correctement initialisés. Si vous n'écrivez pas explicitement `super()`, le compilateur l'ajoute automatiquement dans la première ligne du code, mais seulement si la superclasse a un constructeur sans argument, sauf si nous appelons déjà un autre constructeur via `this()`.
    

Mais n'utilisez pas à la fois les mots-clés `super()` et `this()` dans le même constructeur (vous pouvez les utiliser dans des constructeurs séparés.

Disons qu'il n'a pas de super classe – alors quoi ?

La réponse est simple : Java a une classe Object intégrée qui a un constructeur sans argument par défaut. C'est pourquoi nos classes s'exécutent sans problème même si nous n'écrivons pas super() nous-mêmes, car Java l'appelle en arrière-plan.

Cela signifie que chaque classe que nous créons est une sous-classe de la classe objet :

#### Initialisation des attributs :

À ce stade, les champs sont initialisés :

* D'abord, avec des valeurs par défaut (par exemple, 0 pour int, null pour les objets),
    
* Ensuite, avec toute initialisation explicite que nous avons écrite (par exemple, int x = 10), les valeurs par défaut seront remplacées par celles-ci.
    

#### Exécution du constructeur :

Et enfin, la logique s'exécute. C'est là que tous ou certains des attributs définis dans la classe pour la création d'objets sont initialisés par les paramètres utilisés lors de la création de l'objet, avec l'aide des constructeurs.

Mais tous les champs ne sont pas nécessairement initialisés. Les champs qui ne sont pas mis à jour par le constructeur conserveront les valeurs qu'ils ont déjà (soit la valeur par défaut, soit les valeurs explicitement initialisées).

En bref, le constructeur nous donne la flexibilité de personnaliser notre objet au moment de la création, mais il ne définit pas automatiquement chaque champ à moins que nous n'écrivions explicitement la logique pour cela.

Vérifiez le code ci-dessous pour mieux comprendre :

```java
class Exemple {

    int a;           // par défaut 0
    int b = 10;      // explicitement initialisé à 10
    String nom;     // par défaut null

    Exemple(int x) {
        a = x;       // seul 'a' est défini via le constructeur
        // 'b' n'est pas changé, reste 10
        // 'nom' n'est pas changé, reste null
    }

    void afficher() {
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("nom = " + nom);
    }

    public static void main(String[] args) {
        Exemple obj = new Exemple(5);
        obj.afficher();
    }
}
```

**Sortie :**

![Sortie du code expliquant comment fonctionne le constructeur.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRr6j8-QeGffPm7DYMImJL5s9X-apEGhLzXAv_cNw2CcwONejKxd4-_xKbmdKGSW1w09lt3Pib_psv7RLkd5LJ1uUxd9LSU2KOcDU9kYeqjYbZWS-qUN1PuLbNV8uF0M373kl7Cw?key=-LGNq3k7xufJJBHkVFXMZw align="center")

Dans l'exemple ci-dessus, nous avons trois membres de données – a, b, et nom. Nous avons déjà fait la déclaration et l'initialisation de la variable b au début et donné une valeur à a au moment de la création de l'objet.

Ainsi, nous pouvons voir que :

1. **a**, dont la valeur a été mise à jour par le constructeur avec la valeur donnée au moment de la création de l'objet, a la même valeur
    
2. **b,** qui avait déjà une valeur et ne se met pas à jour par le constructeur, imprime la même valeur
    
3. la chaîne **nom** n'avait pas de valeur, donc null a été imprimé à la place, car c'est la valeur par défaut du type de données String.
    

## **Comment utiliser le mot-clé** `return` **dans les constructeurs**

Nous savons que les constructeurs sont définis sans type de retour, mais nous pouvons utiliser le mot-clé return dans le constructeur uniquement pour quitter le constructeur tôt, et non pour retourner une valeur. Consultez le code ci-dessous.

### **Code d'exemple :**

```java
public class Vélo {

    String nomModèle;  // variable d'instance
    int vitesse;

    // Constructeur paramétré
    Vélo(String modèle, int sp) {
        nomModèle = modèle;
        return;
        vitesse = sp;
    }

    public static void main(String[] args) {
        // Passer le paramètre lors de la création de l'objet Vélo
        Vélo monVélo = new Vélo("Vélo de montagne", 20);
        System.out.println("Objet Vélo créé ! Modèle : " + monVélo.nomModèle);
        System.out.println("La vitesse du Vélo est " + monVélo.vitesse);
    }
}
```

Essayons de comprendre le code ci-dessus et l'utilisation du mot-clé return avec lui. Nous commencerons par ce qui se passerait si le mot-clé return n'était pas ici. Le code se serait exécuté sans aucune erreur et aurait reçu une sortie.

![code sans le mot-clé return](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdRpxqN-7mjbNNenChHDcIxtufG5P4LQOG1GXo4L7_kFz955k-YF2HJfy96ZoIbPtxy3flUKiw4Mq6C8qSdZEnw3bzg5rbAy3BR4Q4x7uO2EjZfN7zFGDRlCWbAth_s97TGvoHpCQ?key=-LGNq3k7xufJJBHkVFXMZw align="center")

Maintenant, que se passera-t-il si nous ajoutons le mot-clé return ? Comme nous l'avons discuté ci-dessus, le mot-clé return indiquera au compilateur de ne pas aller au-delà de ce point dans le constructeur.

Ainsi, tout ce que nous avons écrit dans le constructeur après le mot-clé return ne sera pas compilé, et si cela avait une valeur et était nécessaire pour l'exécution correcte de notre code, le compilateur générera une erreur.

![code avec le mot-clé return](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc63VgyWkEdvcPr8x9TkVb-ZJKuPO2Z-ips_sNT70zGwFYRRdzfYYWG1Bfwnjmdypz-Pt8YS6SwQGBKMNrNhz4J27psGuOxz9Fs0gLVpM0oHzn5N1J0w3wgL7HU7rUQlB200qoRoA?key=-LGNq3k7xufJJBHkVFXMZw align="center")

L'erreur le dit clairement : 'instruction inaccessible', ce qui signifie que le compilateur n'a pas été autorisé à aller au-delà du mot-clé return.

Maintenant que vous comprenez le mot-clé return, voyons quand vous pouvez l'utiliser.

### **Exemple :**

```java
public class Vélo {

    // Constructeur avec une condition pour sortir tôt
    Vélo(boolean skip) {
        if (skip) {
            System.out.println("Le constructeur est sorti tôt");
            return; // Termine l'exécution du constructeur ici
        }

        System.out.println("Le constructeur continue...");
        // Plus de logique d'initialisation peut aller ici
        System.out.println("Objet Vélo initialisé avec succès");
    }

    public static void main(String[] args) {
        System.out.println("Création du premier vélo (skip = true) :");
        Vélo vélo1 = new Vélo(true);  // Le constructeur sortira tôt

        System.out.println("\nCréation du deuxième vélo (skip = false) :");
        Vélo vélo2 = new Vélo(false); // Le constructeur continuera
    }
}
```

Nous avons défini une classe Vélo qui a un constructeur avec un paramètre booléen appelé skip. À l'intérieur du constructeur, il y a une instruction if qui vérifie si skip est vrai. Si c'est le cas, le constructeur imprime un message et utilise le mot-clé return pour sortir tôt. Cela signifie que le reste du constructeur ne s'exécutera pas.

Mais il n'y a pas de bloc else. Alors, que se passe-t-il lorsque skip est faux ? Dans ce cas, la condition if n'est pas vraie, alors le code à l'intérieur de l'instruction if n'est pas exécuté (y compris le mot-clé return) et le constructeur continue simplement aux lignes de code suivantes. C'est là que nous faisons l'initialisation réelle du vélo et imprimons un message de succès.

En bref :

1. Si skip est vrai, le constructeur sort tôt.
    
2. Si skip est faux, le constructeur continue et termine la configuration.
    

![sortie de l'exemple expliquant le mot-clé return](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeK-1kbbG97wMT_d-zrZ28eCuVsWZEkH6Ve3kuYSyXM1e-pZDsJl8K1S4GVfp54XnxGLOGGH_y_B3lZvmy1GRSvOY5Xp_rqHZd7jdNHHxdVAdVuW5vM__6DU99SdS38b03jXjkj?key=-LGNq3k7xufJJBHkVFXMZw align="center")

C'est une manière simple de contrôler combien du constructeur s'exécute, en fonction d'une condition.

## **Conclusion**

Dans ce blog, nous avons compris de nombreux sujets différents, ce qu'est un constructeur, ses différents types, comme le constructeur par défaut, le constructeur sans argument, le constructeur paramétré et le constructeur de copie, non seulement avec la théorie mais aussi avec des exemples de code.

Les comprendre non seulement améliorera notre compréhension mais nous aidera également à écrire un code modulaire et bien maintenu en Java. Bien que ce concept soit également important en POO, car il est centré autour du concept d'objets et les constructeurs sont ceux qui sont utilisés pour les initialiser.

## **Questions fréquemment posées**

**Q1. Pourquoi utilisons-nous des constructeurs ?**

**R :** Nous utilisons des constructeurs parce que :

1. Ils sont créés automatiquement par le compilateur et initialisent l'objet avec des valeurs par défaut.
    
2. Nous pouvons initialiser tous les attributs des objets en une seule fois.
    
3. Ils empêchent l'initialisation incomplète ou incorrecte des objets en garantissant que les données importantes sont fournies lors de la création de l'objet.
    
4. La maintenabilité et la modularité du code augmentent.
    
5. Nous pouvons utiliser des objets dès qu'ils sont créés.
    

**Q2. Quelle est la différence de base entre la surcharge de méthode et la surcharge de constructeur ?**

**R :**

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Caractéristique</strong></p></td><td colspan="1" rowspan="1"><p><strong>Surcharge de méthode</strong></p></td><td colspan="1" rowspan="1" colwidth="256"><p><strong>Surcharge de constructeur</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>But</strong></p></td><td colspan="1" rowspan="1"><p>Effectuer différentes opérations avec le même nom de méthode</p></td><td colspan="1" rowspan="1" colwidth="256"><p>Créer des objets avec différentes initialisations</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Type de retour</strong></p></td><td colspan="1" rowspan="1"><p>Peut avoir un type de retour</p></td><td colspan="1" rowspan="1" colwidth="256"><p>N'a pas de type de retour</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Nom</strong></p></td><td colspan="1" rowspan="1"><p>Peut être n'importe quel nom de méthode valide</p></td><td colspan="1" rowspan="1" colwidth="256"><p>A toujours le même nom que la classe</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Contexte d'utilisation</strong></p></td><td colspan="1" rowspan="1"><p>Appelé sur des objets existants</p></td><td colspan="1" rowspan="1" colwidth="256"><p>Appelé lors de la création d'objets</p></td></tr></tbody></table>

Vous pouvez consulter certains de mes autres articles pour débutants sur mon blog :

1. [Comprendre l'abstraction en Java](https://tekolio.com/what-is-abstraction-in-java-and-how-to-achieve-it/)
    
2. [Comment construire une application de films en React en utilisant l'API TMDB ?](https://tekolio.com/how-to-build-a-movie-app-in-react-using-tmdb-api/)
    
3. [Comment fusionner deux tableaux triés](https://tekolio.com/how-to-merge-two-sorted-arrays/)