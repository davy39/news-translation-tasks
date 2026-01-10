---
title: Comment écrire un programme Java pour obtenir la série Fibonacci
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-28T12:06:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-java-program-to-find-the-fibonacci-series
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/How-to-write-Java-Program-to-find-Fibonacci-Series-2.png
tags:
- name: Java
  slug: java
- name: Math
  slug: math
seo_title: Comment écrire un programme Java pour obtenir la série Fibonacci
seo_desc: "By Bikash Daga (Jain)\nThe Fibonacci Series is a special kind of sequence\
  \ that starts with 0 and 1, and every number after those two is the sum of the two\
  \ preceding numbers. \nThe Fibonacci series goes like this: 0, 1, 1, 2, 3, 5, 8,\
  \ 13, 21, … and so o..."
---

Par Bikash Daga (Jain)

La série Fibonacci est une sorte spéciale de séquence qui commence avec `0` et `1`, et chaque nombre après ceux-ci est la somme des deux nombres précédents. 

La série Fibonacci est la suivante : `0, 1, 1, 2, 3, 5, 8, 13, 21, …` et ainsi de suite. Elle a été décrite pour la première fois dans les mathématiques indiennes.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/calculate-the-Fibonacci-number-we-have-basic-2-approaches.png)
_Source : [Scaler Topics](https://www.scaler.com/topics/fibonacci-series-in-java/)_

La série Fibonacci est utilisée dans de nombreux domaines comme la finance et la technologie. On peut également l'observer dans de nombreux processus naturels.

L'importance de la série Fibonacci dans la nature est magnifiquement expliquée dans la citation de Guy Murchie

> _« La séquence Fibonacci s'avère être la clé pour comprendre comment la nature conçoit... et fait... partie de la même musique omniprésente des sphères qui construisent l'harmonie dans les atomes, les molécules, les cristaux, les coquillages, les soleils, et les galaxies et fait chanter l'Univers. » – **Guy Murchie, Les Sept Mystères de la Vie : Une Exploration de la Science et de la Philosophie**_

### Connaissez-vous ces faits ?

* Le rapport de deux nombres consécutifs dans la série Fibonacci est approximativement **1,6**. Par exemple : **21 / 13 = 1,61 et 55 / 34 = 1,61**
* Le 23 novembre est le jour de Fibonacci, car la date de ce jour ressemble à la série Fibonacci au format **mm/jj** car c'est **(11/23)**.

## Comment calculer la série Fibonacci en utilisant l'approche Top-Down

Dans cette approche Top-Down, nous calculons la valeur de l'index requis comme la somme des valeurs des deux index précédents. 

Si les deux valeurs précédentes ne sont pas disponibles pour nous, nous répétons le même processus pour elles également. 

Si leurs valeurs ne sont également pas disponibles pour nous, nous répétons le même processus jusqu'à ce que nous obtenions les deux valeurs. C'est une approche qui est guidée par la théorie.

Nous utilisons ici une approche de type arbre – nous cherchons simplement les deux valeurs précédentes et si ces valeurs ne sont pas disponibles pour nous, nous répétons le processus jusqu'à ce que nous obtenions les deux valeurs. 

Nous divisons l'algorithme complexe en fragments plus petits qui peuvent être appelés modules. Et nous pouvons diviser ces modules en fragments encore plus petits jusqu'à ce qu'ils ne puissent plus être fragmentés.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Top-Down-Approach.png)
_Source : [Scaler Topics](https://www.scaler.com/topics/fibonacci-series-in-java/)_

### Algorithme pour l'approche Top-Down

Tout d'abord, vous prenez l'entrée 'n' pour obtenir le nombre correspondant dans la série Fibonacci.

Ensuite, vous calculez la valeur de l'index requis comme une somme des valeurs des deux index précédents (c'est-à-dire que vous ajoutez les valeurs des index `n-1` et `n-2`). Si les valeurs ne sont pas trouvées pour les deux index précédents, vous ferez de même pour trouver les valeurs à cet index.

Dès que vous obtenez les valeurs pour les deux index précédents consécutifs, vous les additionnez et retournez le résultat comme valeur pour l'index suivant.

Ensuite, vous additionnez la valeur de l'index « n - 1 » et « n - 2 » et retournez la valeur requise.

### Avantages de l'approche Top-Down

* Le débogage de votre projet devient plus efficace.
* L'implémentation du code devient plus facile.
* Cela rend le code facile à résoudre et à gérer.
* Le processus de test devient plus facile grâce à des modules séparés.

### Inconvénients de l'approche Top-Down

* Il y a une forte dépendance aux autres modules. Les changements dans un module peuvent affecter tous les autres modules.
* C'est une approche plus lente par rapport à l'approche Bottom-Up en programmation dynamique en raison de la récursivité.

## Comment calculer la série Fibonacci en utilisant l'approche Bottom-Up

Dans cette approche Bottom-Up, nous créons un tableau et remplissons les valeurs des deux premiers index avec `0` et `1`, respectivement. 

Après cela, nous calculons la valeur de tous les index en utilisant ces deux valeurs pour les stocker dans un tableau. 

Nous pouvons récupérer la valeur de n'importe quel index pour obtenir le nombre correspondant dans la série Fibonacci.

**Par exemple :** si `fibNum` est un [tableau](https://www.freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example/#:~:text=What%20is%20an%20array%3F,your%20array%20should%20be%20strings.) stockant les nombres Fibonacci, alors nous insérons :

```java
fibNum[0]  = 0 ;  fibNum[1] = 1 ;
```

Ensuite, dans une boucle itérative avec une variable pointeur **i**, nous écrivons :

```java
fibNum[i] = fibNum[ i - 1 ] + fibNum[ i - 2 ] ;
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Bottom-Up-Approach-1.png)
_Source : [Scaler Topics](https://www.scaler.com/topics/)_

### Algorithme pour l'approche Bottom-Up

Tout d'abord, vous prenez l'entrée 'n' pour obtenir le nombre correspondant dans la série Fibonacci.

Ensuite, vous devez stocker les valeurs de la série Fibonacci, donc vous déclarez un tableau de taille 'n' pour cela.

Ensuite, insérez la valeur pour les deux premiers index comme `0` et `1`, respectivement.

Utilisez une boucle itérative pour le troisième et les autres index restants comme décrit dans l'explication ci-dessus.

Enfin, retournez la valeur du dernier index du tableau.

### Avantages de l'approche Bottom-Up

* Il est plus facile de créer des cas de test.
* Votre code est réutilisable
* Il y a moins de redondance grâce à l'encapsulation des données et à la dissimulation des données.

### Inconvénients de l'approche Bottom-Up

* Parfois, elle consomme un espace et un temps supplémentaires.
* Parfois, il est difficile de comprendre le fonctionnement dans les étapes initiales.

## Comment coder la séquence Fibonacci

Il existe plusieurs façons d'écrire un programme pour trouver les nombres Fibonacci en Java.

### 1. Comment coder la séquence Fibonacci en utilisant des boucles itératives simples

Voici comment obtenir le n-ième nombre Fibonacci en Java en utilisant une boucle for :

```java
import java.util.*;
public class fibonacci{
    public static void main(String args[]){
        int n,k;
        Scanner snr= new Scanner(System.in);
        n=snr.nextInt();
        snr.close();
        int array[]=new int[n];
        // L'espace utilisé ici est O(N)
        array[0]=0;
        array[1]=1;
        for(k=2;k<n;k++)array[k]=array[k-1]+array[k-2];
        // Le tableau est parcouru une seule fois donc la complexité temporelle est O(N)
        System.out.println("Le nombre à la position N dans la série Fibonacci est "+array[n-1]);
    }
}
```

Voici comment obtenir le n-ième nombre Fibonacci en Java en utilisant une boucle while :

```java
import java.util.*;
public class fibonacci{
    public static void main(String args[]){
        int n,k;
        Scanner snr= new Scanner(System.in);
        n=snr.nextInt();
        snr.close();
        int array[]=new int[n];
        // L'espace utilisé ici est O(N)
        array[0]=0;
        array[1]=1;
        k=2;
        while(k<n)
            array[k]=array[k-1]+array[k-2];
            k++;
        System.out.println("Le nombre à la position N dans la série Fibonacci est "+array[n-1]);
    }
    // Le tableau est parcouru une seule fois donc la complexité temporelle est O(N)
}
```

#### Complexité temporelle :

La complexité temporelle pour cette approche est `O(N)`, qui est une complexité temporelle linéaire car nous avons parcouru le tableau une seule fois.

#### Complexité spatiale :

La complexité spatiale pour cette approche est `O(N)`, qui est une complexité spatiale linéaire car nous avons stocké les réponses aux sous-problèmes dans un tableau.

### 2. Comment coder la séquence Fibonacci en utilisant la récursivité

Maintenant, nous allons passer en revue l'algorithme pour la série Fibonacci en utilisant la récursivité en Java.

En récursivité, nous utilisons une fonction définie (disons que c'est `fib` ici dans ce code) pour trouver le nombre Fibonacci. 

Dans la fonction `main()`, nous appelons la fonction `fib()` pour le n-ième nombre dans la série Fibonacci.

Nous définissons le cas de base pour cet appel récursif – c'est-à-dire qu'il retourne `0` et `1` pour les 0-ième et 1-er nombres Fibonacci, respectivement. 

Nous allons appeler la fonction à l'intérieur d'elle-même comme `fib( x ) = fib( x-1 ) + fib( x-2)` jusqu'à ce qu'elle atteigne le cas de base et ensuite nous obtiendrons les valeurs à partir de là. 

### Comment obtenir le n-ième nombre Fibonacci en Java en utilisant la récursivité

```java
import java.util.*;
public class fibonacci{
    public static void main(String args[]){
        int n;
        Scanner snr= new Scanner(System.in);
        n=snr.nextInt();
        snr.close();
        System.out.println(fib(n));
//Affichage du nombre dans la série Fibonacci
    }
    public static int fib(int n){
        if(n==0){
            return 0;
        }
        // Cas de base retourne lui-même 0 et 1
        else if(n==1){
            return 1;
        }
        else{
            return fib(n-1)+fib(n-2);
            // Appels récursifs
        }
    }
}
```

#### Complexité temporelle :

La complexité temporelle pour cette approche est `O( 2 ^ N )` qui est une complexité temporelle exponentielle, où n est l'index du n-ième nombre Fibonacci. 

Nous devons trouver les deux valeurs précédentes pour obtenir chaque valeur. Pour cela, nous appelons la fonction deux fois pour chaque valeur et l'arbre peut avoir au plus `n` niveaux.   
  
Cela fait environ `2 ^ n` nœuds dans l'arbre.

#### Complexité spatiale :

La complexité spatiale pour l'approche utilisant la [récursivité](https://www.freecodecamp.org/news/understanding-recursion-in-programming/) est `O( 2 ^ N )`, qui est une complexité spatiale exponentielle où n est l'index du **n-ième** nombre Fibonacci. 

Comme nous devons stocker les valeurs pour chaque nœud et que nous avons `2 ^ N` nœuds, l'espace total dont nous avons besoin pour cela est `2 ^ N`.

### 3. Comment coder la séquence Fibonacci en utilisant la récursivité avec mémoïsation

La mémoïsation signifie que nous continuons à stocker toutes les solutions aux sous-problèmes afin de pouvoir récupérer et utiliser directement la valeur là où nous en avons besoin dans le futur dans le programme. Cela peut nous faire économiser du temps et de l'espace. 

### Algorithme pour la série Fibonacci en utilisant la récursivité en Java

Ici, nous définissons une fonction (nous utilisons `fib()`) et l'utilisons pour trouver notre nombre Fibonacci souhaité. 

Nous déclarons un tableau global suffisamment grand pour stocker tous les nombres Fibonacci une fois calculés. 

Dans la fonction `main()`, nous appelons la fonction `fib()` pour le n-ième nombre. Ensuite, nous définissons les cas de base pour l'appel récursif et retournons `0` et `1`, respectivement, pour les index 0 et 1.

Nous appelons `fib(x) = fib( x-1 ) + fib( x-2 )` pour tous les `x > 2`. Pour chaque valeur calculée, nous la stockons dans le tableau global. 

La valeur de chaque nombre Fibonacci est stockée dans l'index correspondant du tableau global. Ensuite, nous pouvons les récupérer et les utiliser pour des usages ultérieurs. Cela améliore considérablement la complexité temporelle.

### Comment obtenir le n-ième nombre Fibonacci en Java en utilisant la récursivité avec mémoïsation

```java
import java.util.*;
public class fibonacci{
    public static int fib(int n){
        if(n==1){
            return array[0];
        }
        // cas de base
        if(n==2){
            return array[1];
        }
        else{
            array[n-1] = fib(n-1) + fib(n-2);
            return (array [n-1]);
        }
    }
    public static void main(String args[]){
        int n;
        Scanner snr= new Scanner(System.in);
        n=snr.nextInt();
        snr.close();
        array[0]=0;
        array[1]=1;
        System.out.println(fib(n));
        // affichage du nombre dans la série fibonacci
    }
    static int array[]=new int[1000];
    // Déclaration d'un tableau global suffisamment grand
 }
```

#### Complexité temporelle :

La complexité temporelle pour cette approche est `O(  N )` qui est une complexité temporelle linéaire, où `n` est l'index du **n-ième** nombre Fibonacci. 

Nous devons trouver les deux valeurs précédentes pour obtenir chaque valeur – mais ici nous les avons déjà stockées dans un tableau, donc nous devons appeler la fonction une seule fois pour tous les éléments.

#### Complexité spatiale :

La complexité spatiale pour cette approche est `O( N )` qui est une complexité spatiale linéaire, où `n` est l'index du **n-ième** nombre Fibonacci. 

Nous devons stocker uniquement les valeurs pour chaque nœud et nous avons seulement **N** nœuds.

## Conclusion

Dans cet article, nous avons appris comment trouver la série Fibonacci en Java de quatre manières différentes, deux pour l'approche Bottom-Up et deux pour l'approche Top-Down. 

Nous avons également appris que la récursivité avec mémoïsation est la manière la plus efficace en termes de temps et d'espace pour obtenir les nombres Fibonacci.

Dans cet article, nous avons discuté de la complexité spatiale et temporelle de chaque approche ainsi que de leurs algorithmes, avantages et inconvénients.

Bon apprentissage et bon codage !