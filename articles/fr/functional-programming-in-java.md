---
title: Programmation fonctionnelle en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-14T17:34:55.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/lambda.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: Java
  slug: java
seo_title: Programmation fonctionnelle en Java
seo_desc: "By Sameer Shukla\nFunctional programming (FP) is a programming paradigm.\
  \ It emphasizes the use of pure functions that don't have side effects and always\
  \ return the same output for a given input. \nThis article explores how to implement\
  \ FP concepts in J..."
---

Par Sameer Shukla

La programmation fonctionnelle (FP) est un paradigme de programmation. Elle met l'accent sur l'utilisation de fonctions pures qui n'ont pas d'effets de bord et renvoient toujours le même résultat pour une entrée donnée. 

Cet article explore comment implémenter les concepts de FP en Java, notamment en considérant les fonctions comme des citoyens de première classe, en les chaînant et en les composant pour créer des pipelines de fonctions.

Nous aborderons également la technique de la curryfication, qui permet de transformer une fonction prenant plusieurs arguments en une chaîne de fonctions prenant chacune un seul argument. Cela peut simplifier l'utilisation de fonctions complexes et les rendre plus réutilisables. 

Dans cet article, je vais vous montrer des exemples de mise en œuvre de ces concepts en Java en utilisant des fonctionnalités modernes du langage, telles que « java.util.function.Function », « java.util.function.BiFunction » et une TriFunction définie par l'utilisateur. Nous verrons ensuite comment surmonter ses limitations grâce à la curryfication. 

## L'interface `java.util.function.Function` 

L'interface java.util.function.Function est un composant clé de l'API de programmation fonctionnelle de Java 8. La java.util.function.Function est une interface fonctionnelle en Java qui prend une entrée de type 'T' et produit une sortie de type 'R'. 

En programmation fonctionnelle, les fonctions sont des citoyens de première classe, ce qui signifie qu'elles peuvent être manipulées comme des valeurs, stockées dans des variables ou des structures de données, et utilisées comme arguments ou valeurs de retour d'autres fonctions. 

L'interface Function fournit un moyen de définir et de manipuler des fonctions dans le code Java.

L'interface Function représente une fonction qui prend une entrée et produit une sortie. Elle possède une seule méthode abstraite, `apply()`, qui prend un argument d'un type spécifié et renvoie un résultat d'un type spécifié. 

Vous pouvez utiliser l'interface Function pour définir de nouvelles fonctions, ainsi que pour manipuler et composer des fonctions existantes. Par exemple, vous pouvez l'utiliser pour convertir une liste d'objets d'un type en une liste d'objets d'un autre type, ou pour appliquer une série de transformations à un flux (stream) de données.

L'un des principaux avantages de l'interface Function est qu'elle vous permet d'écrire un code plus concis et expressif. En définissant des fonctions comme des valeurs et en les manipulant comme des arguments ou des valeurs de retour, les développeurs peuvent créer un code plus modulaire et réutilisable. De plus, en utilisant des lambdas pour définir des fonctions, le code Java peut être plus expressif et plus facile à lire.

Vous pouvez concevoir `java.util.function.Function` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-98.png)
_Function&lt;A, B&gt;_

La java.util.function.BiFunction est également une interface fonctionnelle en Java qui prend deux entrées 'T' et 'U' et produit une sortie de type 'R'. En résumé, BiFunction prend 2 entrées et renvoie un résultat :

```
BiFunction<Integer, Integer, Integer> sum = (a, b) -> a + b;
```

 Vous pouvez concevoir `java.util.function.BiFunction` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-99.png)
_BiFunction&lt;A, B, C&gt;_

## Composition et chaînage de fonctions

Le chaînage de fonctions est une technique de programmation fonctionnelle qui consiste à composer plusieurs fonctions en un seul pipeline ou une seule chaîne. 

En Java FP, le chaînage de fonctions est souvent utilisé pour transformer des données en une série d'étapes, où chaque étape applique une transformation spécifique aux données et les transmet à l'étape suivante de la chaîne.

L'interface Function en Java fournit un outil puissant pour le chaînage de fonctions. Chaque fonction de la chaîne est définie comme une instance distincte de l'interface Function. La sortie de chaque fonction devient l'entrée de la fonction suivante dans la chaîne. Cela permet d'appliquer une série de transformations aux données, les unes après les autres, jusqu'à ce que le résultat final soit produit.

### Comment utiliser la méthode `andThen` 

La méthode « andThen() » est une méthode par défaut fournie par l'interface Function en Java. Cette méthode prend une séquence de deux fonctions et les applique successivement, en utilisant la sortie de la première fonction comme entrée de la deuxième fonction. Ce chaînage des fonctions aboutit à une nouvelle fonction qui combine le comportement des deux fonctions en une seule transformation. 

La syntaxe de `andThen` ressemble à ceci :

```java
default <V> Function<T, V> andThen(Function<? super R, ? extends V> after) 
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-107.png)
_andThen_

Nous pouvons décomposer l'exemple en une série d'étapes. Initialement, la fonction « multiply » sera exécutée et sa sortie sera transmise en entrée à la fonction « add ». Ensuite, la fonction « logOutput » est utilisée pour enregistrer la sortie résultante. 

```java
public class FunctionChainingExample {

    static Logger logger = Logger.getLogger(FunctionChainingExample.class.getName());

    private static Function<Integer, Integer> multiply = x -> x * 2;

    private static Function<Integer, Integer> add = x -> x + 2;

    private static Function<Integer, Unit> logOutput = x -> {
        logger.info("Data:" + x);
        return Unit.unit();
    };

    public static Unit execute(Integer input) {
        Function<Integer, Unit> pipeline = multiply
                                               .andThen(add)
                                               .andThen(logOutput);
        return pipeline.apply(input);
    }

    public static void main(String[] args) {
        execute(10);
    }

}
```

Le fragment de code ci-dessus illustre la création de trois fonctions, à savoir multiply, add et logOutput. 

La fonction `multiply` accepte une entrée entière et produit une sortie entière, tout comme la fonction `add`. Cependant, la fonction `logOutput` accepte une entrée entière et ne renvoie rien (représenté par l'objet Unit, ce qui implique l'absence de valeur). 

La fonction `execute` chaîne les trois fonctions ensemble, où la sortie de multiply est utilisée comme entrée pour la fonction add, et la sortie résultante de add est transmise à la fonction logOutput à des fins de journalisation. L'exemple ci-dessus illustre le chaînage de fonctions à l'aide de la méthode par défaut `andThen`. 

### Comment utiliser la méthode `compose` 

Contrairement à la méthode `andThen`, la méthode `compose` est une autre méthode par défaut fournie par l'interface Function en Java. Elle applique la première fonction à la sortie de la deuxième fonction. 

Cela signifie que la deuxième fonction est d'abord appliquée à l'entrée, puis la première fonction est appliquée à la sortie de la deuxième fonction. Par conséquent, une chaîne de fonctions est créée où la sortie de la deuxième fonction devient l'entrée de la première fonction. 

La fonction compose ressemble à ceci :

```java
default  Function<V, R> compose(Function<? super V, ? extends T> before)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-118.png)
_compose_

Le choix entre `andThen` et `compose` dépend de l'ordre dans lequel vous souhaitez que les fonctions soient appliquées.

Si vous souhaitez appliquer les fonctions dans l'ordre où elles sont définies, de gauche à droite, vous devez utiliser la méthode `andThen`. Cette méthode applique la première fonction à l'entrée, puis applique la seconde fonction à la sortie de la première fonction. 

Ceci est utile lorsque vous souhaitez chaîner des fonctions qui traitent les données d'entrée dans un ordre spécifique.

D'un autre côté, si vous souhaitez appliquer les fonctions dans l'ordre inverse, de droite à gauche, vous devez utiliser la méthode `compose`. Cette méthode applique la seconde fonction à l'entrée, puis applique la première fonction à la sortie de la seconde fonction. 

Ceci est utile lorsque vous souhaitez chaîner des fonctions qui doivent être appliquées dans l'ordre inverse de la manière dont elles sont définies.

En général, vous devriez utiliser `andThen` lorsque vous voulez appliquer les fonctions dans l'ordre défini, et `compose` lorsque vous voulez les appliquer dans l'ordre inverse. Mais le choix entre les deux méthodes dépend en fin de compte des exigences spécifiques de votre cas d'utilisation.

```
 public static Unit compose(Integer input) {
        Function<Integer, Unit> pipeline = logOutput
                                            .compose(add)
                                            .compose(multiply);
        return pipeline.apply(input);
    }
```

Dans l'exemple `compose`, les fonctions sont exécutées dans un ordre de droite à gauche. Premièrement, `multiply` est exécutée et sa sortie est transmise à la fonction `add`. Ensuite, la sortie résultante de la fonction `add` est transmise à `logOutput` pour journalisation.

### Comment utiliser la fonction `apply()` 

La méthode `apply()` prend une entrée et renvoie un résultat. Elle est utilisée pour appliquer une fonction à un argument et calculer un résultat.

La fonction `apply()` est une méthode d'interfaces fonctionnelles, telle que l'interface Function, qui prend un argument d'un type spécifié et renvoie un résultat d'un type spécifié. C'est l'unique méthode abstraite de ces interfaces, ce qui est nécessaire pour qu'elles soient utilisées comme interfaces fonctionnelles.

La fonction `apply()` définit le comportement de l'interface fonctionnelle. Lorsqu'une instance d'une interface fonctionnelle est créée, la fonction `apply()` est implémentée pour définir ce que fait l'interface fonctionnelle lorsqu'elle est appelée avec un argument.

```
Function<Integer, Integer> multiply = x -> x * x;
        int result = multiply.apply(5);
```

Dans ce code, nous définissons une fonction nommée `multiply` qui prend un argument entier et renvoie le carré de cet entier. Nous appelons ensuite la fonction `apply()` sur cette fonction, en passant la valeur entière 5. La fonction `apply()` exécute l'expression lambda définie dans la Function `multiply`, et renvoie le résultat du calcul, qui est ici 25.

Analysons cela à travers un exemple concret, FileReaderPipeline.

```
public class FileReaderPipeline {

    static Function<String, String> trim = String::trim;
    static Function<String, String> toUpperCase = String::toUpperCase;
    static Function<String, String> replaceSpecialCharacters = 
    	str -> str.replaceAll("[^\\p{Alpha}]+", "");

    static Function<String, String> pipeline = 
                                trim
                                  .andThen(toUpperCase)
                                  .andThen(replaceSpecialCharacters);

 public static void main(String[] args) throws IOException {
        try (BufferedReader reader = new BufferedReader(new 	FileReader("example.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String result = pipeline.apply(line);
                System.out.println(result);
            }
        }
    }
}
```

Le code ci-dessus définit une classe FileReaderPipeline, qui lit des lignes à partir d'un fichier, les traite via un pipeline de fonctions et affiche le résultat final.

Premièrement, trois fonctions `trim`, `toUpperCase`, et `replaceSpecialCharacters` sont définies à l'aide de références de méthodes et d'expressions lambda. `trim` supprime les espaces de début et de fin d'une String, `toUpperCase` convertit la chaîne en majuscules, et `replaceSpecialCharacters` supprime tous les caractères non alphabétiques de la chaîne.

Ensuite, un pipeline de fonctions est créé à l'aide de la méthode `andThen`, qui chaîne les trois fonctions. L'entrée de la fonction pipeline est une String, et la sortie est également une String. Lorsqu'une String est transmise à la fonction pipeline, elle supprime d'abord les espaces de début ou de fin, puis convertit la chaîne en majuscules, et enfin supprime tout caractère non alphabétique.

Enfin, dans la méthode `main`, le programme lit les lignes d'un fichier (dans cet exemple, « example.txt ») à l'aide d'un `BufferedReader`. Chaque ligne est traitée par la fonction pipeline à l'aide de la méthode `apply`, qui applique chaque fonction du pipeline en séquence et renvoie le résultat. Le résultat est ensuite affiché dans la console via `System.out.println`.

## Curryfication (Currying)

Le package java.util contient deux interfaces fonctionnelles connues sous les noms de « Function<A, B> » et « BiFunction<A, B, C> ». L'interface `Function` prend une seule entrée et produit une sortie, tandis que l'interface `BiFunction` prend deux entrées et produit une sortie. Voici une illustration :

```
 Function<String, String> toUpper = str -> str.toUpperCase();
 BiFunction<Integer, Integer, Integer> sum = (a, b) -> a + b;
```

C'est une contrainte claire car il n'existe que deux fonctions, l'une acceptant une seule entrée et l'autre deux. Par conséquent, si nous avons besoin d'une fonction qui prend trois entrées, nous devons construire notre propre fonction personnalisée.

À cette fin, concevons une fonction qui accepte trois entrées et nommons-la `TriFunction`. Voici un exemple d'implémentation :

```
@FunctionalInterface
public interface TriFunction<A, B, C, O> {
    O apply(A a, B b, C c);

    default <R> TriFunction<A, B, C, O> andThen(TriFunction<A, B, C, O> after) {
        return (A a, B b, C c) -> after.apply(a,b,c);
    }
}
```

```
TriFunction<Integer, Integer, Integer, Integer> sum = (a, b, c) -> a + b + c;																
int result = sum.apply(1, 2, 3);
```

Dans les situations où nous avons besoin de plus de paramètres que ce que les fonctions disponibles peuvent accepter, nous pouvons exploiter la curryfication pour surmonter cette limitation. 

Nous pouvons refactoriser la fonction précédente en utilisant la curryfication, ce qui consiste à décomposer une fonction qui prend plusieurs arguments en une séquence de fonctions, chacune n'acceptant qu'un seul argument. Cela est conforme à la définition de la curryfication, qui est une technique employée en programmation fonctionnelle.

```
Function<Integer, Function<Integer, Function<Integer, Integer>>> 	sumWithThreeParams = (a) -> (b) -> (c) -> a + b + c;
                                                                       Function<Integer, Function<Integer, Function<Integer, Function<Integer, Integer>>>> sumWithFourParams = (a)->(b)->(c)->(d) -> a + b + c + d; 
                                                                                                                    
                                                                                                                 
                                                                                                                         
```

Ce qui précède déclare une nouvelle `Function` nommée `sumWithThreeParams` qui prend une entrée `Integer`. Elle renvoie une nouvelle `Function` qui prend une entrée `Integer` et renvoie encore une autre nouvelle `Function` qui prend une entrée `Integer` et produit une sortie `Integer`. De la même manière, une nouvelle Function nommée `sumWithFourParams` est créée. 

Notez que les fonctions curryfiées `sumWithThreeParams` et `sumWithFourParams` nous permettent d'appliquer partiellement des arguments à la fonction, ce qui peut être utile dans des situations où nous disposons de certaines entrées mais pas de toutes.

```
Function<Integer, Function<Integer, Integer>> partialSumWithTwoParams 									= sumWithThreeParams.apply(5);
                                                                        Function<Integer, Integer> partialSumWithOneParams 
								 = partialSumWithTwoParams.apply(10);

                                                                        int c = 15;
int result = partialSumWithOneParams.apply(c);
System.out.println(result); //30
```

## Conclusion

Dans cet article, nous avons abordé la mise en œuvre des concepts de programmation fonctionnelle (FP) en Java, tels que le traitement des fonctions comme des citoyens de première classe, leur composition en pipelines et l'utilisation de la curryfication pour simplifier les fonctions complexes.

Nous avons fourni des exemples utilisant des fonctionnalités modernes du langage comme `java.util.function.Function` et `java.util.function.BiFunction`, ainsi qu'une `TriFunction` définie par l'utilisateur avec curryfication pour surmonter ses limitations.

En appliquant ces techniques, les développeurs peuvent écrire un code plus concis, réutilisable et maintenable en Java.

Avec la popularité croissante de la FP dans l'industrie, comprendre et mettre en œuvre ces concepts devient de plus en plus important pour les développeurs Java.

Après avoir lu cet article, si vous l'avez trouvé utile et souhaitez explorer plus d'exemples pratiques, [veuillez visiter le dépôt](https://github.com/sameershukla/JavaFPLearning) et envisagez de lui donner une étoile.