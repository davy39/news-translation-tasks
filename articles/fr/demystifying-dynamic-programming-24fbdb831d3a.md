---
title: Démystifier la programmation dynamique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T00:28:32.000Z'
originalURL: https://freecodecamp.org/news/demystifying-dynamic-programming-24fbdb831d3a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Tyqzs42Dpy2qPZHpcm2HoQ.png
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Démystifier la programmation dynamique
seo_desc: 'By Prajwal M

  There are many quality articles on how to become a software developer. They teach
  you to program, develop, and use libraries. But little has been done to educate
  in Algorithms and DataStructures. No matter how good you are at development...'
---

Par Prajwal M

Il existe de nombreux articles de qualité sur la façon de devenir développeur logiciel. Ils vous apprennent à programmer, à développer et à utiliser des bibliothèques. Mais peu a été fait pour éduquer en **Algorithmes** et **Structures de données**_. Peu importe à quel point vous êtes bon en développement, sans connaissance des **Algorithmes** et des **Structures de données**_, vous ne pouvez pas être embauché_._

Apprendre des algorithmes populaires comme **Multiplication de chaînes de matrices, Sac à dos ou Voyageur de commerce** **Algorithmes** n'est pas suffisant. Les recruteurs posent des problèmes comme ceux que vous trouvez sur les sites de programmation compétitive. Pour résoudre de tels problèmes, vous devez avoir une bonne et solide compréhension des concepts.

#### **Qu'est-ce que la programmation dynamique ?**

Selon [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming), la programmation dynamique consiste à simplifier un problème compliqué en le décomposant en sous-problèmes plus simples de manière [récursive](https://en.wikipedia.org/wiki/Recursion). Cet article vous apprendra à :

```
-> Identifier les sous-problèmes
-> Apprendre à résoudre les sous-problèmes
-> Identifier que les sous-problèmes sont répétitifs 
-> Identifier que les sous-problèmes ont une propriété de sous-structure optimale
-> Apprendre à mettre en cache/stocker les résultats des sous-problèmes
-> Développer une relation récursive pour résoudre le problème
-> Utiliser une approche descendante et ascendante pour résoudre le problème
```

#### **Quel langage vais-je utiliser ?**

Je sais que la plupart des gens sont compétents ou ont de l'expérience en codage en JavaScript. De plus, une fois que vous avez appris en JavaScript, il est très facile de le transformer en code Java. La même chose peut être dite pour Python ou C++. Le truc est de comprendre les problèmes dans le langage que vous préférez le plus. J'ai donc choisi d'utiliser JavaScript.

**Cet article parle des algorithmes et plus spécifiquement de la programmation dynamique. Il est généralement perçu comme un sujet difficile. Si vous arrivez à la fin de l'article, je suis sûr que vous pourrez résoudre de nombreux problèmes de programmation dynamique par vous-même** ?.

### **Énoncé du problème**

```
Problème : Étant donné un entier n, trouvez le nombre minimum d'étapes pour atteindre l'entier 1.

À chaque étape, vous pouvez :

Soustraire 1,

Diviser par 2, s'il est divisible par 2

Diviser par 3, s'il est divisible par 3
```

Tous les problèmes de programmation dynamique ont un **état de départ**. Vous devez atteindre l'**objectif** en **transitionnant** à travers un **nombre d'états intermédiaires**. Dans un manuel typique, vous entendrez souvent le terme **sous-problème**. C'est la même chose qu'un **état**. Les termes peuvent être utilisés de manière interchangeable. Dans cet article, j'utiliserai le terme état au lieu du terme sous-problème.

**Qu'est-ce qu'un sous-problème ou un état ?** Un sous-problème/état est une instance plus petite du problème original. Les méthodes utilisées pour résoudre le problème original et le sous-problème sont les mêmes.

> _Certains problèmes vous donneront les règles qui spécifient les transitions d'état. C'est l'un de ces problèmes. Ce problème dit que vous pouvez passer à n-1, n/2 ou n/3 en partant de n. D'un autre côté, il y a des problèmes qui ne spécifieront pas les transitions d'état. Vous devrez les découvrir par vous-même. Je parlerai de ces types de problèmes dans un autre article._

Ici,

```
État de départ -> n
Objectif -> 1
États intermédiaires -> n'importe quel nombre entier entre 1 et n
```

Étant donné un état (soit de départ soit intermédiaire), **vous pouvez toujours passer à un nombre fixe d'états**.

```
à partir de n vous pouvez passer à :

n -> n-1 

si n % 2 == 0:
   n -> n/2
   
si n % 3 == 0:
   n -> n/3
   
exemple:

à partir de 3 vous pouvez passer à,
3 -> 3-1 = 2
3 -> 3/3 = 1

à partir de 4 vous pouvez passer à,
4 -> 4-1 = 3
4 -> 4/2 = 2
```

Dans un problème d'optimisation de programmation dynamique_, vous devez déterminer **en passant par quels états du début à l'objectif vous obtiendrez une solution optimale**.

```
Pour n = 4:

approche une:
4 -> 3 -> 2 -> 1

approche deux:
4 -> 2 -> 1 

approche trois:
4 -> 3 -> 1
```

Ici, parmi les trois approches, les approches deux et trois sont optimales, car elles nécessitent le plus petit nombre de mouvements/transitions. L'approche une est la pire, car elle nécessite plus de mouvements.

#### **Terminologies du manuel expliquées**

```
Sous-problèmes répétitifs : Vous finirez par résoudre le même problème plus d'une fois.

pour n = 5
exemple:
5 -> 4 -> 3 -> 1
5 -> 4 -> 2 -> 1
5 -> 4 -> 3 -> 2 -> 1

observez ici que 2 -> 1 se produit deux fois. 
observez également que 5 -> 4 se produit trois fois.

Sous-structure optimale : Les solutions optimales aux sous-problèmes donnent une solution optimale à l'ensemble du problème

exemple:
2 -> 1 est optimal 
3 -> 1 est optimal 

quand je suis à 4,
4 -> 3 -> 2 -> 1 et 4 -> 3 -> 1 est possible
mais la solution optimale de 4 est 4 -> 3 -> 1. La solution optimale de quatre vient de la solution optimale de trois (3 -> 1).

de même,
4 -> 3 -> 2 -> 1 et 4 -> 2 -> 1 est possible
mais la solution optimale de 4 est 4 -> 2 -> 1. La solution optimale de quatre vient de la solution optimale de deux (2 -> 1).

maintenant 5,
La solution optimale de 5 dépend de la solution optimale à 4.
5 -> 4 -> 2 -> 1 et 5 -> 4 -> 3 -> 1 sont optimales.
```

**Comment utiliser les sous-problèmes répétitifs et la sous-structure optimale à notre avantage ?**

> _Nous résoudrons les sous-problèmes une seule fois et résoudrons chaque sous-problème de manière optimale._

```
Nous résoudrons les sous-problèmes 3 -> 1 et 2 -> 1 une seule fois et de manière optimale.

Maintenant pour 4, nous résoudrons une seule fois par 4 -> 3 -> 1 et de manière optimale. Vous pouvez également résoudre comme 4 -> 2 -> 1 mais cela vous est laissé. 

Enfin pour 5, nous résoudrons une seule fois par 5 - > 4 -> 3 -> 1 et de manière optimale.
```

En pratique, vous utiliserez un tableau pour stocker le résultat optimal d'un sous-problème. Ainsi, lorsque vous devez résoudre le sous-problème à nouveau, vous pouvez obtenir la valeur à partir du tableau plutôt que de le résoudre à nouveau. Essentiellement, vous ne résolvez maintenant un sous-problème qu'une seule fois.

#### **Comment mesurer l'optimalité**

En utilisant quelque chose appelé **coût**. Il y a toujours un coût associé au passage d'un état à un autre état. Le coût peut être zéro ou un nombre fini. L'ensemble des mouvements/transitions qui donnent le coût optimal est la solution optimale.

```
Dans 5 -> 4 -> 3 -> 1 
pour 5 -> 4 le coût est 1 
pour 4 -> 3 le coût est 1
pour 3 -> 1 le coût est 1

Le coût total de 5 -> 4 -> 3 -> 1 est la somme totale de 3.

Dans 5 -> 4 -> 3 -> 2 -> 1
pour 5 -> 4 le coût est 1
pour 4 -> 3 le coût est 1 
pour 3 -> 2 le coût est 1
pour 2 -> 1 le coût est 1
Le coût total de 5 -> 3 -> 2 -> 1 est la somme totale de 4.

La solution optimale de 5 -> 4 -> 3 -> 1 a un coût de trois qui est le minimum. Par conséquent, nous pouvons voir que les solutions optimales ont des coûts optimaux
```

**Relation récursive :** Tous les problèmes de programmation dynamique ont des relations récursives. **Une fois que vous avez défini une relation récursive, la solution consiste simplement à la traduire en code.**

```
Pour le problème ci-dessus, définissons minOne comme la fonction que nous utiliserons pour résoudre le problème et le coût de passage d'un état à un autre comme 1.

si n = 5,
la solution pour 5 est coût + solution pour 4
la formule/relation récursive est 
minOne(5) = 1 + minOne(4) 

De même,
si n = 6,
la formule/relation récursive est
minOne(6) = min(             
              1 + minOne(5),
              1 + minOne(3),
              1 + minOne(2) )
```

### **Code**

Les problèmes de programmation dynamique peuvent être résolus par une approche **descendante** ou une approche **ascendante**.

```
Descendante : Résoudre les problèmes de manière récursive. 
pour n = 5, vous résoudrez/commencerez par 5, c'est-à-dire par le haut du problème.
C'est une approche relativement facile à condition d'avoir une bonne maîtrise de la récursivité. Je dis que cette approche est facile car cette méthode est aussi simple que de transformer votre relation récursive en code.

Ascendante : Résoudre les problèmes de manière itérative.
pour n = 5, vous résoudrez/commencerez par 1, c'est-à-dire par le bas du problème.
Cette approche utilise une boucle for. Elle ne conduit pas à un débordement de pile comme dans la récursivité. Cette approche est également légèrement plus optimale.
```

#### **Quelle approche est meilleure ?**

Cela dépend de votre confort. Les deux donnent les mêmes solutions. Dans les problèmes très grands, l'approche ascendante est bénéfique car elle ne conduit pas à un débordement de pile. Si vous choisissez une entrée de 10000, l'approche descendante donnera une taille maximale de pile de dépassée, mais une approche ascendante vous donnera la solution.

Mais n'oubliez pas que vous ne pouvez pas éliminer complètement la pensée récursive. Vous devrez toujours définir une relation récursive indépendamment de l'approche que vous utilisez.

#### **Approche ascendante**

```js
/*
Problème : Étant donné un entier n, trouvez le nombre minimum d'étapes pour atteindre l'entier 1.
À chaque étape, vous pouvez :
Soustraire 1,
Diviser par 2, s'il est divisible par 2 
Diviser par 3, s'il est divisible par 2 
*/


// ascendante
function minOneBottomUp(n) {

    const cache = [];
    // condition de base
    cache[1] = 0;

    for (i = 2; i <= n; i++) {

        // initialiser a, b et c à des nombres très grands
        let a = 1000, b = 1000, c = 1000;

        // une étape de i -> i-1
        a = 1 + cache[i - 1];

        // une étape de i -> i/2 si i est divisible par 2
        if (i % 2 === 0) {
            b = 1 + cache[i / 2];
        }

        // une étape de i -> i/3 si i est divisible par 3
        if (i % 3 === 0) {
            c = 1 + cache[i / 3];
        }

        // Stocker le nombre minimum d'étapes pour atteindre i
        cache[i] = Math.min(a, b, c);
    }

    // retourner le nombre minimum d'étapes pour atteindre n
    return cache[n];
}

console.log(minOneBottomUp(1000));
```

```
Ligne 11 : La fonction qui résoudra le problème est nommée minOneBottomUp. Elle prend n comme entrée.

Ligne 13 : Le tableau qui sera utilisé pour stocker les résultats de chaque état résolu afin qu'il n'y ait pas de calcul répété est nommé cache. Certaines personnes aiment appeler le tableau dp au lieu de cache. En général, cache[i] est interprété comme le nombre minimum d'étapes pour atteindre 1 en partant de i.

Ligne 15 : cache[1] = 0 Il s'agit de la condition de base. Elle indique que le nombre minimum d'étapes pour atteindre 1 en partant de 1 est 0.

Ligne 17 - 37 : Boucle for pour remplir le cache avec tous les états de 1 à n inclus.

Ligne 20 : Initialiser les variables a, b et c à un grand nombre. Ici, a représente le nombre minimum d'étapes. Si j'ai fait l'opération n-1, b représente le nombre minimum d'étapes. Si j'ai fait l'opération n/2, c représente le nombre minimum d'étapes. Si j'ai fait l'opération n/3. Les valeurs initiales de a, b et c dépendent de la taille du problème.

Ligne 23 : a = 1 + cache[i-1]. Cela suit la relation récursive que nous avons définie précédemment.

Ligne 26 - 28: if(i % 2 == 0){
                  b = 1 + cache[i/2];
              }
              
Cela suit la relation récursive que nous avons définie précédemment.

Ligne 31 - 33: if(i % 3== 0){
                  c= 1 + cache[i/3];
              }
Cela suit la relation récursive que nous avons définie précédemment.

Ligne 36 : Il s'agit de l'étape la plus importante.
cache[i] = Math.min(a, b, c). Cela détermine et stocke essentiellement lequel de a, b et c a donné le nombre minimum d'étapes.

Ligne 40 : Tous les calculs sont terminés. Le nombre minimum d'étapes pour tous les états de 1 à n est calculé. Je retourne cache[n](nombre minimum d'étapes pour atteindre 1 en partant de n) qui est la réponse que nous voulions.

Ligne 43 : Code de test. Il retourne une valeur de 9
```

#### **Approche descendante**

```js
/*
Problème : Étant donné un entier n, trouvez le nombre minimum d'étapes pour atteindre l'entier 1.
À chaque étape, vous pouvez :
Soustraire 1,
Diviser par 2, s'il est divisible par 2 
Diviser par 3, s'il est divisible par 2 
*/


// descendante
function minOne(n, cache) {

    // si la valeur du tableau à n n'est pas indéfinie, retourner la valeur à cet indice
    // C'est le cœur de la programmation dynamique 
    if (typeof (cache[n]) !== 'undefined') {
        return cache[n];
    }

    // si n a atteint 1, retourner 0
    // condition de terminaison/de base
    if (n <= 1) {
        return 0;
    }

    // initialiser a, b et c à des nombres très grands
    let a = 1000, b = 1000, c = 1000;

    // une étape de n -> n-1
    a = 1 + minOne(n - 1, cache);

    // une étape de n -> n/2 si n est divisible par 2
    if (n % 2 === 0) {
        b = 1 + minOne(n / 2, cache);
    }

    // une étape de n -> n/3 si n est divisible par 3
    if (n % 3 === 0) {
        c = 1 + minOne(n / 3, cache);
    }

    // Stocker le nombre minimum d'étapes pour atteindre n 
    return cache[n] = Math.min(a, b, c);

}



const cache = [];
console.log(minOne(1000, cache));
```

```
Ligne 11 : La fonction qui résoudra le problème est nommée minOne. Elle prend n et cache comme entrées.

Ligne 15 - 16 : Elle vérifie si pour un état particulier la solution a été calculée ou non. Si elle est calculée, elle retourne la valeur précédemment calculée. C'est la manière descendante de ne pas faire de calcul répété.

Ligne 21 - 23 : Il s'agit de la condition de base. Elle indique que si n est 1, le nombre minimum d'étapes est 0.

Ligne 26 : Initialiser les variables a, b et c à un grand nombre. Ici, a représente le nombre minimum d'étapes si j'ai fait l'opération n-1, b représente le nombre minimum d'étapes si j'ai fait l'opération n/2 et c représente le nombre minimum d'étapes si j'ai fait l'opération n/3. Les valeurs initiales de a, b et c dépendent de la taille du problème.

Ligne 29 : a = 1 + minOne(n-1, cache). Cela suit la relation récursive que nous avons définie précédemment.

Ligne 32 - 34 : if(n % 2 == 0){
                  b = 1 + minOne(n/2, cache);
              }
Cela suit la relation récursive que nous avons définie précédemment.

Ligne 37 - 39 : if(n % 3== 0){
                  c = 1 + minOne(n/3, cache);
              }
Cela suit la relation récursive que nous avons définie précédemment.

Ligne 42 : return cache[n] = Math.min(a, b, c). Cela détermine et stocke essentiellement lequel de a, b et c a donné le nombre minimum d'étapes.

Ligne 48 - 49 : Code de test. Il retourne une valeur de 9
```

#### **Complexité temporelle**

Dans les problèmes de programmation dynamique, la complexité temporelle est **le nombre d'états/sous-problèmes uniques * temps pris par état**.

Dans ce problème, pour un n donné, il y a **n** états/sous-problèmes uniques. Pour plus de commodité, on dit que chaque état est résolu en un temps constant. Par conséquent, la complexité temporelle est **O(n * 1)**.

Cela peut être facilement vérifié par la boucle for que nous avons utilisée dans l'approche ascendante. Nous voyons que nous utilisons seulement une boucle for pour résoudre le problème. Par conséquent, la complexité temporelle est **O(n) ou linéaire.**

C'est la puissance de la programmation dynamique. Elle permet de résoudre efficacement des problèmes aussi complexes.

#### **Complexité spatiale**

Nous utilisons un tableau appelé cache pour stocker les résultats de n états. Par conséquent, la taille du tableau est n. Par conséquent, la complexité spatiale est **O(n)**.

#### **DP comme compromis espace-temps**

La programmation dynamique utilise l'espace pour résoudre un problème plus rapidement. Dans ce problème, nous utilisons **O(n)** d'espace pour résoudre le problème en **O(n)** de temps. Par conséquent, nous échangeons de l'espace pour de la vitesse/temps. Par conséquent, il est aptement appelé le **compromis espace-temps**.

### Conclusion

J'espère que cet article démystifie la programmation dynamique. Je comprends que la lecture de l'ensemble de l'article a pu être douloureuse et difficile, mais la programmation dynamique est un sujet difficile. La maîtriser nécessite beaucoup de pratique.

Je publierai plus d'articles sur la démystification de différents types de problèmes de programmation dynamique. Je publierai également un article sur la façon de transformer une solution de retour en arrière en une solution de programmation dynamique.

Si vous aimez cet article, veuillez soutenir en applaudissant ?(vous pourriez aller jusqu'à 50) et suivez-moi ici sur Medium f44f. Vous pouvez vous connecter avec moi sur [LinkedIn](https://www.linkedin.com/in/prajwalm/). Vous pouvez également me suivre sur [Github](https://github.com/PrajwalM2212).