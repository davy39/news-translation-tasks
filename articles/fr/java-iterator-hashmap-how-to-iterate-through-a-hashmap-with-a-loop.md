---
title: Java Iterator Hashmap – Comment parcourir une Hashmap avec une boucle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T18:01:21.000Z'
originalURL: https://freecodecamp.org/news/java-iterator-hashmap-how-to-iterate-through-a-hashmap-with-a-loop
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-Java-Iterator-Hashmap
seo_title: Java Iterator Hashmap – Comment parcourir une Hashmap avec une boucle
---

How-to-Iterate-Through-a-Hashmap-With-a-Loop.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "Par Shittu Olumide\nHashmap est une structure de données utilisée en programmation pour stocker\n  \ des données sous forme de paires clé-valeur. Elle est largement utilisée dans de nombreux langages de programmation, notamment\n  \ Java, Python et JavaScript. \nParcourir une hashmap est une opération courante\n  \ que les développeurs effectuent fréquemment. Dans cet article, nous allons parcourir un aperçu détaillé de la façon de parcourir une hashmap avec une boucle en Java, en utilisant différents types de boucles.\n"
---

Par Shittu Olumide

Hashmap est une structure de données utilisée en programmation pour stocker des données sous forme de paires clé-valeur. Elle est largement utilisée dans de nombreux langages de programmation, notamment Java, Python et JavaScript.

Parcourir une hashmap est une opération courante que les développeurs effectuent fréquemment. Dans cet article, nous allons parcourir un aperçu détaillé de la façon de parcourir une hashmap avec une boucle en Java, en utilisant différents types de boucles.

La plupart du temps, les étapes impliquées dans le processus de parcours d'une hashmap sont assez simples. Tout d'abord, vous initialisez la hashmap, utilisez un itérateur pour parcourir la hashmap, et enfin affichez votre résultat.

## Comment parcourir une Hashmap Java en utilisant une boucle `for-each`

L'une des façons les plus simples de parcourir une hashmap est d'utiliser une boucle for-each. Voici un exemple de la façon de procéder :

```java
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
map.put("C", 3);

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    String key = entry.getKey();
    Integer value = entry.getValue();
    System.out.println("Clé : " + key + ", Valeur : " + value);
}

```

Dans cet exemple, nous créons d'abord une nouvelle hashmap et ajoutons quelques paires clé-valeur. Nous utilisons ensuite une boucle for-each pour parcourir la hashmap, en récupérant chaque paire clé-valeur sous forme d'objet `Map.Entry`. Nous extrayons ensuite la clé et la valeur de chaque objet Map.Entry et les affichons dans la console.

## Comment parcourir une Hashmap Java en utilisant une boucle `while` avec un `Iterator`

Une autre façon de parcourir une hashmap est d'utiliser une boucle `while` avec un `Iterator`. Voici un exemple de la façon de procéder :

```java
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
map.put("C", 3);

Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
while (iterator.hasNext()) {
    Map.Entry<String, Integer> entry = iterator.next();
    String key = entry.getKey();
    Integer value = entry.getValue();
    System.out.println("Clé : " + key + ", Valeur : " + value);
}

```

Dans cet exemple, nous créons à nouveau une nouvelle hashmap et ajoutons quelques paires clé-valeur. Nous créons ensuite un nouvel objet Iterator en utilisant la méthode `entrySet()`, qui retourne un ensemble de paires clé-valeur sous forme d'objets `Map.Entry`. Nous utilisons ensuite une boucle while avec les méthodes `hasNext()` et `next()` pour parcourir l'ensemble et récupérer chaque paire clé-valeur. Nous extrayons ensuite la clé et la valeur de chaque objet Map.Entry et les affichons dans la console.

## Comment parcourir une Hashmap Java en utilisant une boucle `for` avec `keySet()`

En Java, la méthode `keySet()` est une méthode de la classe `java.util.HashMap` qui retourne une vue `Set` des clés contenues dans la hashmap. Cela signifie qu'elle retourne un ensemble de toutes les clés de la hashmap qui peut être utilisé pour parcourir les clés ou effectuer d'autres opérations sur elles.

La méthode `keySet()` retourne un `Set` des clés de la hashmap, qui est une collection d'éléments uniques sans doublons. Cela est dû au fait que les clés dans une hashmap doivent être uniques, et la méthode `keySet()` garantit que l'ensemble de clés qu'elle retourne ne contient pas de valeurs en double.

Nous pouvons parcourir une hashmap en utilisant une boucle for avec la méthode `keySet()`. Voici un exemple de la façon de procéder :

```java
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
map.put("C", 3);

for (String key : map.keySet()) {
    Integer value = map.get(key);
    System.out.println("Clé : " + key + ", Valeur : " + value);
}

```

Dans cet exemple, nous créons à nouveau une nouvelle hashmap et ajoutons quelques paires clé-valeur. Nous utilisons ensuite une boucle for avec la méthode `keySet()` pour parcourir la hashmap, en récupérant chaque clé et en l'utilisant pour obtenir la valeur correspondante de la hashmap. Nous affichons ensuite à la fois la clé et la valeur dans la console.

## Conclusion

Dans cet article, vous avez appris trois façons de parcourir une hashmap en utilisant différents types de boucles. En suivant ces directives, vous pouvez devenir plus compétent dans le travail avec les hashmaps et autres structures de données.

Il est également important de garder à l'esprit que la modification de la hashmap pendant l'itération peut entraîner des résultats inattendus, donc, lorsque cela est possible, vous devriez éviter de le faire.

Restons en contact sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !