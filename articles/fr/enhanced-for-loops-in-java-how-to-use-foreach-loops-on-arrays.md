---
title: Boucles For améliorées en Java – Comment utiliser les boucles ForEach sur les
  tableaux
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-17T00:55:10.000Z'
originalURL: https://freecodecamp.org/news/enhanced-for-loops-in-java-how-to-use-foreach-loops-on-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/java-enhanced-loop.png
tags:
- name: Java
  slug: java
- name: Loops
  slug: loops
seo_title: Boucles For améliorées en Java – Comment utiliser les boucles ForEach sur
  les tableaux
seo_desc: "You can use enhanced loops in Java to achieve the same results as a for\
  \ loop. An enhanced loop is also known as a for-each loop in Java. \nEnhanced loops\
  \ simplify the way you create for loops. They are mostly used to iterate through\
  \ an array or collec..."
---

Vous pouvez utiliser des boucles améliorées en Java pour obtenir les mêmes résultats qu'avec une boucle [`for`](https://www.freecodecamp.org/news/java-for-loop-example/). Une boucle améliorée est également connue sous le nom de boucle `for-each` en Java.

Les boucles améliorées simplifient la façon dont vous créez des boucles `for`. Elles sont principalement utilisées pour parcourir un tableau ou une collection de variables.

Dans ce tutoriel, vous apprendrez la syntaxe et comment utiliser la boucle `for-each` (boucle améliorée) en Java.

## Syntaxe de la boucle For-Each en Java

Voici à quoi ressemble la syntaxe d'une boucle `for-each` en Java :

```java
for(dataType variable : array) {
    // code à exécuter
}
```

Dans la syntaxe ci-dessus :

* **dataType** désigne le type de données du **tableau**.
* **variable** désigne une variable assignée à chaque élément du tableau lors de l'itération (vous comprendrez cela à travers les exemples qui suivent).
* **array** désigne le tableau à parcourir.

## Exemple de boucle For-Each en Java

Examinons quelques exemples pour vous aider à comprendre comment fonctionne une boucle `for-each`.

### Exemple de boucle For-Each en Java #1

```java
class ForEachExample {
    public static void main(String[] args) {
        
        int[] even_numbers = { 2, 4, 6, 8 };
        
        for(int number : even_numbers){
           System.out.println(number);
           // 2
           // 4
           // 6
           // 8
        }
        
    }
}
```

Dans le code ci-dessus, nous avons créé un tableau appelé `even_numbers`.

Pour parcourir et imprimer tous les nombres du tableau, nous avons utilisé une boucle `for-each` : `for(int number : even_numbers){...}`.

Dans les parenthèses de la boucle, nous avons créé une variable entière appelée `number` qui serait utilisée pour parcourir le tableau `even_numbers`.

Ainsi, pour :

#### Itération #1

`number` = premier élément du tableau (2). Cela est imprimé.

#### Itération #2

`number` = deuxième élément du tableau (4). Cette valeur actuelle est imprimée.

#### Itération #3

`number` = troisième élément du tableau (6). Cette valeur actuelle est imprimée.

#### Itération #4

`number` = quatrième élément du tableau (8). Cette valeur actuelle est imprimée.

La valeur de `number` change pour correspondre à l'index actuel pendant le processus d'itération jusqu'à ce qu'elle atteigne la fin du tableau. Après chaque index imprimé, elle passe à l'index suivant.

Vous pouvez également voir cela ainsi : "Pour chaque `number` dans le tableau `even_numbers`, imprimer `number`".

### Exemple de boucle For-Each en Java #2

```java
class ForEachExample {
    public static void main(String[] args) {
        
        int[] even_numbers = { 2, 4, 6, 8 };
        
        for(int number : even_numbers){
            number = number*2;
            System.out.println(number);
        }
        
    }
}
```

Dans le code ci-dessus, nous multiplions la valeur de chaque élément par deux en utilisant la variable `number` : `number = number*2;`.

Le processus ici est le même que dans le dernier exemple. Lorsque `number` devient un élément du tableau, il double la valeur de l'élément et l'imprime dans la console.

## Résumé

Vous pouvez utiliser des boucles `for-each` en Java pour parcourir les éléments d'un tableau ou d'une collection.

Elles simplifient la création de boucles `for`. Par exemple, la syntaxe d'une boucle `for` nécessite que vous créiez une variable, une condition qui spécifie quand la boucle doit se terminer, et une valeur d'incrément/décrément.

Avec les boucles `for-each`, tout ce dont vous avez besoin est une variable et le tableau à parcourir.

Mais cela ne signifie pas que vous devriez toujours opter pour les boucles `for-each`.

Les boucles `for` vous donnent plus de contrôle sur ce qui se passe pendant le processus d'itération – contrôler et suivre ce qui se passe à chaque index ou à certains index.

D'autre part, les boucles `for-each` peuvent être utilisées lorsque vous n'avez pas besoin de suivre chaque index. Le code parcourt simplement chaque élément du tableau.

Vous pouvez en apprendre plus sur les boucles `for` en Java en [lisant cet article](https://www.freecodecamp.org/news/java-for-loop-example/).

Bon codage !