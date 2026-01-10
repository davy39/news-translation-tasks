---
title: Qu'est-ce que le hachage ? Comment fonctionnent les codes de hachage - avec
  des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T22:44:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-hashing
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d75740569d1a4ca37e1.jpg
tags:
- name: Hash tables
  slug: hash-tables
- name: toothbrush
  slug: toothbrush
seo_title: Qu'est-ce que le hachage ? Comment fonctionnent les codes de hachage -
  avec des exemples
seo_desc: 'Introduction to hashing

  Hashing is designed to solve the problem of needing to efficiently find or store
  an item in a collection.

  For example, if we have a list of 10,000 words of English and we want to check if
  a given word is in the list, it would ...'
---

## Introduction au hachage

Le hachage est conçu pour résoudre le problème de besoin de trouver ou de stocker un élément dans une collection de manière efficace.

Par exemple, si nous avons une liste de 10 000 mots anglais et que nous voulons vérifier si un mot donné est dans la liste, il serait inefficace de comparer successivement le mot avec tous les 10 000 éléments jusqu'à ce que nous trouvions une correspondance. Même si la liste de mots est triée lexicographiquement, comme dans un dictionnaire, vous aurez toujours besoin de temps pour trouver le mot que vous cherchez.

Le hachage est une technique pour rendre les choses plus efficaces en réduisant effectivement la recherche dès le départ.

## **Qu'est-ce que le hachage ?**

Le hachage signifie utiliser une fonction ou un algorithme pour mapper les données d'un objet à une valeur entière représentative.

Ce code de hachage (ou simplement hachage) peut ensuite être utilisé comme un moyen de réduire notre recherche lors de la recherche de l'élément dans la map.

Généralement, ces codes de hachage sont utilisés pour générer un index, à lequel la valeur est stockée.

## **Comment fonctionne le hachage**

Dans les tables de hachage, vous stockez les données sous forme de paires clé-valeur. La clé, qui est utilisée pour identifier les données, est donnée comme entrée à la fonction de hachage. Le code de hachage, qui est un entier, est ensuite mappé à la taille fixe que nous avons.

Les tables de hachage doivent supporter 3 fonctions.

* insert (clé, valeur)
* get (clé)
* delete (clé)

Purement à titre d'exemple pour nous aider à comprendre le concept, supposons que nous voulons mapper une liste de clés de chaînes à des valeurs de chaînes (par exemple, mapper une liste de pays à leurs capitales).

Donc, disons que nous voulons stocker les données dans la Table dans la map.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-15-at-2.53.40-PM.png)

Et supposons que notre fonction de hachage est simplement de prendre la longueur de la chaîne.

Pour simplifier, nous aurons deux tableaux : un pour nos clés et un pour les valeurs. 
Donc, pour mettre un élément dans la table de hachage, nous calculons son code de hachage (dans ce cas, nous comptons simplement le nombre de caractères), puis nous mettons la clé et la valeur dans les tableaux à l'index correspondant.

Par exemple, Cuba a un code de hachage (longueur) de 4. Donc, nous stockons Cuba à la 4ème position dans le tableau des clés, et La Havane à la 4ème index du tableau des valeurs, etc. Et nous obtenons ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-15-at-2.54.43-PM.png)

Maintenant, dans cet exemple spécifique, les choses fonctionnent assez bien. Notre tableau doit être assez grand pour accueillir la chaîne la plus longue, mais dans ce cas, cela ne fait que 11 emplacements. 
Nous gaspillons un peu d'espace parce que, par exemple, il n'y a pas de clés d'une lettre dans nos données, ni de clés entre 8 et 10 lettres. 

Mais dans ce cas, l'espace gaspillé n'est pas si mauvais non plus. Prendre la longueur d'une chaîne est rapide et agréable, et le processus de recherche de la valeur associée à une clé donnée est également rapide (certes plus rapide que de faire jusqu'à cinq comparaisons de chaînes).

Mais, que faisons-nous si notre ensemble de données contient une chaîne qui a plus de 11 caractères ? 
Que se passe-t-il si nous avons un autre mot de 5 caractères, "India", et que nous essayons de l'assigner à un index en utilisant notre fonction de hachage. Puisque l'index 5 est déjà occupé, nous devons décider quoi faire avec. Cela s'appelle une collision.

Si notre ensemble de données avait une chaîne avec mille caractères, et que vous créez un tableau de mille indices pour stocker les données, cela entraînerait un gaspillage d'espace. Si nos clés étaient des mots aléatoires en anglais, où il y a tant de mots de même longueur, utiliser la longueur comme fonction de hachage serait assez inutile.

## **Gestion des collisions**

Deux méthodes de base sont utilisées pour gérer les collisions.

1. Chaînage séparé
2. Adressage ouvert

### Chaînage séparé

La gestion des collisions de hachage par chaînage séparé utilise une structure de données supplémentaire, de préférence une liste chaînée pour l'allocation dynamique, dans des compartiments. Dans notre exemple, lorsque nous ajoutons l'Inde à l'ensemble de données, elle est ajoutée à la liste chaînée stockée à l'index 5, puis notre tableau ressemblerait à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-15-at-2.55.47-PM.png)

Pour trouver un élément, nous allons d'abord au compartiment puis nous comparons les clés. C'est une méthode populaire, et si une liste de liens est utilisée, le hachage ne se remplit jamais. Le coût pour `get(k)` est en moyenne `O(n)` où n est le nombre de clés dans le compartiment, le nombre total de clés étant N.

Le problème avec le chaînage séparé est que la structure de données peut croître sans limites.

### Adressage ouvert

L'adressage ouvert n'introduit aucune nouvelle structure de données. Si une collision se produit, nous cherchons la disponibilité dans l'emplacement suivant généré par un algorithme. L'adressage ouvert est généralement utilisé lorsque l'espace de stockage est restreint, c'est-à-dire les processeurs embarqués. L'adressage ouvert n'est pas nécessairement plus rapide que le chaînage séparé.

Méthodes pour l'adressage ouvert

* [Sondage linéaire](https://en.wikipedia.org/wiki/Linear_probing)
* [Sondage quadratique](https://en.wikipedia.org/wiki/Quadratic_probing)
* [Double hachage](https://en.wikipedia.org/wiki/Double_hashing)

## **Comment utiliser le hachage dans votre code.**

#### **Python**

```text
   # Quelques langages comme Python, Ruby viennent avec un support de hachage intégré.
   # Déclaration
    my_hash_table = {}
    my_hash_table = dict()

   # Insertion
    my_hash_table[clé] = valeur

   # Recherche
    valeur = my_hash_table.get(clé) # retourne None si la clé n'est pas présente || Différé en python 3, disponible en python 2
    valeur = my_hash_table[clé] # lève une exception ValueError si la clé n'est pas présente

    # Suppression
    del my_hash_table[clé] # lève une exception ValueError si la clé n'est pas présente

    # Obtenir toutes les clés et valeurs stockées dans le dictionnaire
    clés = my_hash_table.keys()
    valeurs = my_hash_table.values()
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CVtK)

#### **Java**

```text
    // Java n'inclut pas le hachage par défaut, vous devez l'importer depuis la bibliothèque java.util
    // Importation des hashmap
    import java.util.HashMap;

   // Déclaration
    HashMap<Integer, Integer> myHashTable = new HashMap<Integer, Integer>(); // déclare une map vide.

   // Insertion
    myHashTable.put(clé, valeur);

   // Suppression
    myHashtable.remove(clé);

   // Recherche
    myHashTable.get(clé); // retourne null si la clé K n'est pas présente
    myHashTable.containsKey(clé); // retourne une valeur booléenne, indiquant la présence d'une clé

    // Nombre de paires clé, valeur dans la table de hachage
    myHashTable.size();
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CVt1)

## Plus d'informations sur le hachage

* [Le guide sans code du hachage et des tables de hachage](https://www.freecodecamp.org/news/the-codeless-guide-to-hash/)
* [Comment implémenter une table de hachage simple en JavaScript](https://www.freecodecamp.org/news/how-to-implement-a-simple-hash-table-in-javascript-cb3b9c1f2997/)
* [Tables de hachage expliquées](https://www.freecodecamp.org/news/hash-tables/)