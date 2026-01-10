---
title: 'Table de hachage expliquée : qu''est-ce que c''est et comment l''implémenter'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T18:11:00.000Z'
originalURL: https://freecodecamp.org/news/hash-tables
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8e740569d1a4ca385f.jpg
tags:
- name: data structures
  slug: data-structures
seo_title: 'Table de hachage expliquée : qu''est-ce que c''est et comment l''implémenter'
seo_desc: A hash table, also known as a hash map, is a data structure that maps keys
  to values. It is one part of a technique called hashing, the other of which is a
  hash function. A hash function is an algorithm that produces an index of where a
  value can be ...
---

Une table de hachage, également connue sous le nom de carte de hachage, est une structure de données qui mappe des clés à des valeurs. Elle fait partie d'une technique appelée hachage, dont l'autre partie est une fonction de hachage. Une fonction de hachage est un algorithme qui produit un index où une valeur peut être trouvée ou stockée dans la table de hachage.

Quelques points importants sur les tables de hachage :

1. Les valeurs ne sont pas stockées dans un ordre trié.
2. Vous devez tenir compte des collisions potentielles. Cela se fait généralement avec une technique appelée chaînage. Le chaînage signifie créer une liste liée de valeurs, dont les clés mappent à un certain index.

## Implémentation d'une table de hachage

L'idée de base derrière le hachage est de distribuer les paires clé/valeur dans un tableau de placeholders ou "buckets" dans la table de hachage.

Une table de hachage est typiquement un tableau de listes liées. Lorsque vous souhaitez insérer une paire clé/valeur, vous devez d'abord utiliser la fonction de hachage pour mapper la clé à un index dans la table de hachage. Étant donné une clé, la fonction de hachage peut suggérer un index où la valeur peut être trouvée ou stockée :

```text
index = f(key, array_size)
```

Cela se fait souvent en deux étapes :

```text
hash = hashfunc(key)
index = hash % array_size
```

En utilisant cette méthode, `hash` est indépendant de la taille de la table de hachage. `hash` est réduit à un index – un nombre entre 0, le début du tableau, et `array_size - 1`, la fin du tableau – en utilisant l'opérateur modulo (%).

Considérons la chaîne suivante, `S` :

```text
string S = "ababcd"
```

Vous devez compter la fréquence de tous les caractères dans `S`. La manière la plus simple de faire cela est d'itérer à travers tous les caractères possibles et de compter la fréquence de chacun, un par un.

Cela fonctionne, mais c'est lent – la complexité temporelle d'une telle approche est O(26*N), avec `N` étant la taille de la chaîne `S` multipliée par 26 caractères possibles de A-Z.

```c
void countFre(string S)
    {
        for(char c = 'a';c <= 'z';++c)
        {
            int frequency = 0;
            for(int i = 0;i < S.length();++i)
                if(S[i] == c)
                    frequency++;
            cout << c << ' ' << frequency << endl;
        }
    }
```

**Sortie :**

```text
a 2
b 2
c 1
d 1
e 0
f 0
...
z 0
```

Regardons une solution qui utilise le hachage.

Prenez un tableau et utilisez la fonction de hachage pour hacher les 26 caractères possibles avec des indices du tableau. Ensuite, itérez sur `S` et augmentez la valeur du caractère actuel de la chaîne avec l'index correspondant pour chaque caractère.

La complexité de cette approche de hachage est O(N), où N est la taille de la chaîne.

```text
int Frequency[26];

    int hashFunc(char c)
    {
        return (c - 'a');
    }

    void countFre(string S)
    {
        for(int i = 0;i < S.length();++i)
        {
            int index = hashFunc(S[i]);
            Frequency[index]++;
        }
        for(int i = 0;i < 26;++i)
            cout << (char)(i+'a') << ' ' << Frequency[i] << endl;
    }
```

Sortie

```text
a 2
b 2
c 1
d 1
e 0
f 0
...
z 0
```

## Collisions de hachage

Puisque votre carte de hachage sera probablement significativement plus petite que la quantité de données que vous traitez, les collisions de hachage sont inévitables. Il existe deux approches principales pour gérer les collisions : le *chaînage* et l'*adressage ouvert*.

### Chaînage

Comme mentionné précédemment, le chaînage signifie que chaque paire clé/valeur dans la table de hachage, la valeur est une liste liée de données plutôt qu'une seule cellule.

Par exemple, imaginez que la clé 152 contient la valeur "John Smith". Si la valeur "Sandra Dee" est ajoutée à la même clé, "Sandra Dee" est ajoutée comme un autre élément à la clé 152, juste après "John Smith".

```
152: [["John Smith", "p01"]]

...

152: [["John Smith", "p01"] ["Sandra Dee", "p02"]]
```

Le principal inconvénient du chaînage est l'augmentation de la complexité temporelle. Au lieu de O(1) comme avec une table de hachage régulière, chaque recherche prendra plus de temps puisque nous devons parcourir chaque liste liée pour trouver la valeur correcte.

### Adressage ouvert

L'adressage ouvert signifie que, une fois qu'une valeur est mappée à une clé déjà occupée, vous vous déplacez le long des clés de la table de hachage jusqu'à ce que vous en trouviez une qui est vide. Par exemple, si "John Smith" était mappé à 152, "Sandra Dee" sera mappé à l'index ouvert suivant :

```
152: ["John Smith", "p01"] 

...

152: ["John Smith", "p01"],
153: ["Sandra Dee", "p02"]
```

Le principal inconvénient de l'adressage ouvert est que, lorsque vous recherchez des valeurs, elles ne sont peut-être pas à la clé map que vous attendez. Au lieu de cela, vous devez parcourir différentes parties de la table de hachage pour trouver la valeur que vous recherchez.