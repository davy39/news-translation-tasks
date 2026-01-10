---
title: Comment écrire un meilleur code Java en utilisant la correspondance de motifs
  et les classes scellées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-11T15:48:42.000Z'
originalURL: https://freecodecamp.org/news/write-better-java-code-pattern-matching-sealed-classes
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Pattern-Matching.png
tags:
- name: Java
  slug: java
seo_title: Comment écrire un meilleur code Java en utilisant la correspondance de
  motifs et les classes scellées
seo_desc: "By Sameer Shukla\nThis article explores how you can improve your Java code\
  \ quality using Pattern Matching and Sealed Classes. \nJava Pattern Matching allows\
  \ you to write more concise and readable code when working with complex data structures.\
  \ It simpl..."
---

Par Sameer Shukla

Cet article explore comment vous pouvez améliorer la qualité de votre code Java en utilisant la correspondance de motifs et les classes scellées. 

La correspondance de motifs en Java vous permet d'écrire un code plus concis et plus lisible lorsque vous travaillez avec des structures de données complexes. Elle simplifie l'extraction de données à partir de structures de données et l'exécution d'opérations sur celles-ci. 

Plongeons-nous dans le sujet et apprenons-en davantage sur la correspondance de motifs et les classes scellées.

## Qu'est-ce que la correspondance de motifs en Java ?

La correspondance de motifs fait correspondre une valeur à un motif qui inclut des variables et des conditions. Si la valeur correspond au motif, les parties correspondantes de la valeur sont liées aux variables du motif. Cela permet d'écrire un code plus lisible et plus intuitif. 

Il existe deux types de correspondance de motifs : traditionnelle et moderne. Examinons les différences entre les deux dans les sections suivantes.

### Correspondance de motifs traditionnelle

Dans la correspondance de motifs traditionnelle, l'instruction `switch` est étendue pour prendre en charge la correspondance de motifs en ajoutant le mot-clé `case` avec un argument de motif. L'instruction `switch` peut correspondre à un type primitif, des wrappers, des énumérations et des chaînes de caractères.

Par exemple :

```java
private static void printGreetingBasedOnInput(String input){
        switch (input){
            case "hello":
                System.out.println("Bonjour");
                break;
            case "goodbye":
                System.out.println("À bientôt !");
                break;
            case "thank you":
                System.out.println("Je vous en prie");
                break;
            default:
                System.out.println("Je ne comprends pas");
                break;
        }
    }
```

La méthode Java `printGreetingBasedOnInput` prend une chaîne `input` et imprime un message de salutation correspondant en fonction de sa valeur en utilisant une instruction switch-case. Elle couvre les cas pour "hello", "goodbye" et "thank you", fournissant des réponses appropriées, et par défaut "Je ne comprends pas" pour toute autre entrée.

### Correspondance de motifs moderne

Dans la correspondance de motifs moderne, l'instruction `switch` peut correspondre à une variété de motifs comme tout type d'objets, d'énumérations ou de primitives. Le mot-clé `case` est utilisé pour spécifier le motif à faire correspondre.

```java
private static void printGreetingBasedOnInput(String input){
        switch (input){
            case "hello" -> System.out.println("Bonjour");
            case "goodbye" -> System.out.println("À bientôt !");
            case "thank you" -> System.out.println("Je vous en prie");
            default -> System.out.println("Je ne comprends pas");
        }
    }
```

Ce fragment de code utilise une syntaxe plus concise. Il simplifie le code en spécifiant directement l'action à effectuer pour chaque étiquette de cas. 

Avant Java 16, nous devions vérifier le type de l'objet puis le caster explicitement en une variable. L'opérateur `instanceof` amélioré introduit dans Java 16 peut à la fois vérifier le type et effectuer un cast implicite vers une variable, comme dans l'exemple ci-dessous : 

```java
private static void printType(Object input){
        switch (input) {
            case Integer i -> System.out.println("Integer");
            case String s -> System.out.println("String!");
            default -> System.out.println("Je ne comprends pas");
        }
    }
```

L'amélioration de `instanceof` devient particulièrement utile lors de l'utilisation de gardes de motifs. Les gardes de motifs sont un moyen de rendre les instructions de cas dans la correspondance de motifs Java plus spécifiques en incluant des expressions booléennes. 

Cela permet un contrôle plus fin sur la manière dont les motifs sont appariés et peut rendre le code plus lisible et plus expressif.

```java
private static void printType(Object input){                                                 
    switch (input) {                                                                         
        case Integer i && i > 10 -> System.out.println("Integer est supérieur à 10");        
        case String s && !s.isEmpty()-> System.out.println("String!");                       
        default -> System.out.println("Entrée invalide");                                      
    }                                                                                        
}                                                                                            
```

Sur la base des exemples présentés ci-dessus, vous pouvez espérer voir que la correspondance de motifs Java offre divers avantages :

* Elle améliore la lisibilité du code en permettant une correspondance efficace des valeurs avec des motifs et en extrayant des données.
* Elle réduit la duplication de code en gérant différents cas avec un seul morceau de code.
* Elle améliore la sécurité des types en permettant la correspondance des valeurs avec des types spécifiques.
* Les gardes de motifs peuvent être utilisés dans les cas pour améliorer davantage la lisibilité et la maintenabilité du code.

## Que sont les classes scellées en Java ?

Les classes scellées permettent aux développeurs de restreindre l'ensemble des classes qui peuvent étendre ou implémenter une classe ou une interface donnée. 

Les classes scellées fournissent un moyen de créer une hiérarchie de classes ou d'interfaces qui peuvent être étendues ou implémentées par un ensemble spécifié de classes uniquement.

Par exemple :

```java
public sealed class Result permits Success, Failure {
    protected String response;

    public String message(){
        return response;
    }
}

public final class Success extends Result {

    @Override
    public String message() {
        return "Succès !";
    }
}

public final class Failure extends Result {

    @Override
    public String message() {
        return "Échec !";
    }
}

```

Dans cet exemple, nous avons défini une classe scellée appelée `Result` qui peut être étendue par les classes `Success` ou `Failure`. 

Toute autre classe qui tente d'étendre `Result` entraînera une erreur de compilation.

Cela fournit un moyen de restreindre l'ensemble des classes qui peuvent être utilisées pour étendre `Result`, rendant le code plus maintenable et extensible.

### Quelques points importants à garder à l'esprit :

* Si une sous-classe souhaite être une sous-classe autorisée d'une classe scellée en Java, elle doit être définie dans le même package que la classe scellée. Si la sous-classe n'est pas définie dans le même package, une erreur de compilation se produira.
* Si une sous-classe est autorisée à étendre une classe scellée en Java, elle doit avoir l'un des trois modificateurs suivants : final, sealed ou non-sealed.
* Une sous-classe scellée doit définir le même ensemble ou un ensemble plus restrictif de sous-classes autorisées que sa superclasse scellée. Les sous-classes scellées doivent être soit finales, soit scellées. Les sous-classes non scellées ne sont pas autorisées en tant que sous-classes autorisées d'une superclasse scellée et toutes les sous-classes autorisées doivent appartenir au même package que la superclasse scellée.

## Comment combiner la correspondance de motifs Java et les classes scellées

Vous pouvez utiliser des classes scellées et leurs sous-classes autorisées dans des instructions switch avec la correspondance de motifs. 

Cela peut rendre le code plus concis et plus facile à lire. Voici un exemple :

```java
private static String checkResult(Result result){                                     
    return switch (result) {                                                          
        case Success s -> s.message();                                                
        case Failure f -> f.message();                                                
        default -> throw new IllegalArgumentException("Entrée inattendue : " + result); 
    };                                                                                
}                                                                                     
```

Dans le cas des classes scellées, le compilateur exige une branche par défaut dans la correspondance de motifs pour s'assurer que tous les cas possibles sont couverts. 

Puisque les classes scellées ont un ensemble fixe de sous-classes autorisées, il est possible de couvrir tous les cas avec un nombre fini d'instructions de cas.

Si une branche par défaut n'est pas incluse, il est possible d'ajouter une nouvelle sous-classe à la hiérarchie à l'avenir, ce qui ne serait pas couvert par les instructions de cas existantes. Cela entraînerait une erreur d'exécution, qui pourrait être difficile à déboguer.

En exigeant une branche par défaut, le compilateur garantit que le code est complet et couvre tous les cas possibles, même si de nouvelles sous-classes sont ajoutées à la hiérarchie de classes scellées à l'avenir. 

Cela aide à prévenir les erreurs d'exécution et rend le code plus robuste et maintenable. 

Si nous modifions la classe `Result` pour inclure une nouvelle sous-classe appelée `Pending` et que nous ne l'avons pas incluse dans notre correspondance de motifs, elle sera couverte par la branche par défaut.

## Qu'est-ce qu'une interface scellée en Java ?

Lors de l'utilisation d'une interface scellée en Java, le compilateur n'exigera pas de branche par défaut dans la correspondance de motifs si tous les cas sont couverts.

Dans le cas où une branche est manquante, le compilateur exigera une branche par défaut pour s'assurer que tous les cas possibles sont gérés. 

Nous sommes toujours tenus d'inclure la branche par défaut lors de l'utilisation de classes scellées. Voici un exemple de code :

```java
public sealed interface OtherResult permits Pending, Timeout {
    void message();
}

public final class Pending implements OtherResult{
    @Override
    public void message() {
        System.out.println("En attente !");
    }
}

public final class Timeout implements OtherResult{
    @Override
    public void message() {
        System.out.println("Timeout !");
    }
}

private static void checkResult(OtherResult result){
        switch (result) {
            case Pending p -> p.message();
            case Timeout t -> t.message();
        };
    }

```

## Conclusion

Voici quelques points clés à retenir concernant l'utilisation de la correspondance de motifs et des classes scellées dans le code Java :

* **Lisibilité améliorée** : La correspondance de motifs et les classes scellées peuvent rendre le code plus expressif et plus facile à lire, car elles permettent une syntaxe plus concise et plus intuitive.
* **Contrôle accru sur les hiérarchies de classes** : Les classes scellées fournissent un moyen de contrôler les hiérarchies de classes et de s'assurer que seules les sous-classes autorisées peuvent être utilisées. Cela peut améliorer la sécurité et la maintenabilité du code.
* **Sécurité de type implicite** : La correspondance de motifs et les classes scellées fournissent une sécurité de type implicite, ce qui peut réduire le risque d'erreurs d'exécution et faciliter la maintenance du code.
* **Réduction de la duplication de code** : La correspondance de motifs et les classes scellées peuvent réduire la duplication de code en permettant de gérer différents cas dans un seul morceau de code.
* **Meilleure organisation du code** : Les classes scellées peuvent aider à organiser le code et à réduire la complexité des hiérarchies de classes en regroupant les classes apparentées.
* **Maintenabilité améliorée** : La correspondance de motifs et les classes scellées peuvent améliorer la maintenabilité du code en le rendant plus facile à comprendre et à mettre à jour, ce qui peut faire gagner du temps et des efforts à long terme.

Merci beaucoup pour votre lecture.