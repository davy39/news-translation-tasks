---
title: Types de données structurés en C - Struct et Typedef expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/structured-data-types-in-c-struct-and-typedef-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf9740569d1a4ca3531.jpg
tags:
- name: c programming
  slug: c-programming
- name: toothbrush
  slug: toothbrush
seo_title: Types de données structurés en C - Struct et Typedef expliqués avec des
  exemples
seo_desc: 'During your programming experience you may feel the need to define your
  own type of data. In C this is done using two keywords: struct and typedef. Structures
  and unions will give you the chance to store non-homogenous data types into a single
  collec...'
---

Au cours de votre expérience en programmation, vous pourriez ressentir le besoin de définir votre propre type de données. En C, cela se fait à l'aide de deux mots-clés : `struct` et `typedef`. Les structures et les unions vous donneront l'opportunité de stocker des types de données non homogènes dans une seule collection.

## **Déclaration d'un nouveau type de données**

```c
typedef struct student_structure{
    char* name;
    char* surname;
    int year_of_birth;
}student;
```

Après ce petit code, `student` sera un nouveau mot-clé réservé et vous pourrez créer des variables de type `student`. Veuillez noter que ce nouveau type de variable sera structuré, ce qui signifie qu'il définit une liste physiquement groupée de variables à placer sous un seul nom dans un bloc de mémoire.

## **Utilisation du nouveau type de données**

Créons maintenant une nouvelle variable `student` et initialisons ses attributs :

```c
   student stu;
 
   strcpy( stu.name, "John");
   strcpy( stu.surname, "Snow"); 
   stu.year_of_birth = 1990;
 
   printf( "Nom de l'étudiant : %s\n", stu.name);
   printf( "Prénom de l'étudiant : %s\n", stu.surname);
   printf( "Année de naissance de l'étudiant : %d\n", stu.year_of_birth);
```

Comme vous pouvez le voir dans cet exemple, vous devez attribuer une valeur à toutes les variables contenues dans votre nouveau type de données. Pour accéder à une variable de structure, vous pouvez utiliser le point comme dans `stu.name`. Il existe également une manière plus courte d'attribuer des valeurs à une structure :

```c
typedef struct{
   int    x;
   int    y;
}point;

point image_dimension = {640,480};
```

Ou si vous préférez définir ses valeurs dans un ordre différent :

```c
point img_dim = { .y = 480, .x = 640 };
```

## **Unions vs Structures**

Les unions sont déclarées de la même manière que les structures, mais sont différentes car un seul élément de l'union peut être utilisé à la fois.

```c
typedef union{
      int circle;
      int triangle;
      int ovel;
}shape;
```

Vous devriez utiliser `union` dans les cas où une seule condition sera appliquée et une seule variable sera utilisée. N'oubliez pas que nous pouvons également utiliser notre tout nouveau type de données :

```c
typedef struct{
      char* model;
      int year;
}car_type;

typedef struct{
      char* owner;
      int weight;
}truck_type;

typedef union{
  car_type car;
  truck_type truck;
}vehicle;
```

## **Quelques astuces supplémentaires**

* Lorsque vous créez un pointeur vers une structure en utilisant l'opérateur `&`, vous pouvez utiliser l'opérateur unaire spécial `->` pour le déréférencer. Cela est très utilisé, par exemple, lorsque vous travaillez avec des listes chaînées en C.
* Le nouveau type défini peut être utilisé comme les autres types de base pour presque tout. Essayez, par exemple, de créer un tableau de type `student` et voyez comment cela fonctionne.
* Les structures peuvent être copiées ou assignées, mais vous ne pouvez pas les comparer !

## Plus d'informations :

* [The C Beginner's Handbook: Learn C Programming Language basics in just a few hours](https://www.freecodecamp.org/news/the-c-beginners-handbook/)
* [Data Types in C - Integer, Floating Point, and Void Explained](https://www.freecodecamp.org/news/structured-data-types-in-c-struct-and-typedef-explained-with-examples/www.freecodecamp.org/news/data-types-in-c-integer-floating-point-and-void-explained/)
* [malloc in C: Dynamic Memory Allocation in C Explained](https://www.freecodecamp.org/news/structured-data-types-in-c-struct-and-typedef-explained-with-examples/www.freecodecamp.org/news/malloc-in-c-dynamic-memory-allocation-in-c-explained/)