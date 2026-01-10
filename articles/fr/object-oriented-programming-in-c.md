---
title: Programmation Orientée Objet en C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T18:03:00.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e69740569d1a4ca3cf0.jpg
tags:
- name: c programming
  slug: c-programming
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Programmation Orientée Objet en C++
seo_desc: "Object oriented programming, OOP for short, aims to implement real world\
  \ entities like inheritance, hiding and polymorphism in programming. \nThe main\
  \ aim of OOP is to bind together the data and the functions that operate on them\
  \ so that no other part..."
---

La programmation orientée objet, ou POO en abrégé, vise à implémenter des entités du monde réel comme l'héritage, le masquage et le polymorphisme en programmation. 

Le principal objectif de la POO est de lier ensemble les données et les fonctions qui opèrent sur elles afin qu'aucune autre partie du code ne puisse accéder à ces données sauf cette fonction.

Apprenons les différentes caractéristiques d'un langage de programmation orienté objet.

### **Objet :**

Les objets sont des entités de base à l'exécution dans un système orienté objet. Les objets sont des instances d'une classe qui sont des types de données définis par l'utilisateur.

```cpp
class person
{
    char name[20];
    int id;
public:
    void getdetails(){}
};
 
int main()
{
   person p1; // p1 est un objet
}
```

Les objets occupent de l'espace en mémoire et ont une adresse associée comme un enregistrement en Pascal ou une structure ou union en C.

Lorsqu'un programme est exécuté, les objets interagissent en s'envoyant des messages les uns aux autres.

Chaque objet contient des données et du code pour manipuler les données. Les objets peuvent interagir sans avoir à connaître les détails des données ou du code des autres. Il suffit de connaître le type de message accepté et le type de réponse retourné par les objets.

### **Classe :**

Une classe est un plan de données et de fonctions ou méthodes. Une classe n'occupe aucun espace.

```cpp
class class_name
{
  private:
     // déclarations des membres de données et des fonctions membres
  public:
     // déclarations des membres de données et des fonctions membres
  protected:
     // déclarations des membres de données et des fonctions membres
};
```

La classe est un type de données défini par l'utilisateur comme les structures et les unions en C.

Par défaut, les variables de classe sont privées, mais dans le cas d'une structure, elles sont publiques. Dans l'exemple ci-dessus, person est une classe.

### **Encapsulation et Abstraction des données :**

Le fait de regrouper (combiner) des données et des fonctions en une seule unité est appelé encapsulation. Les données ne sont pas accessibles au monde extérieur et seules les fonctions qui encapsulent la classe peuvent y accéder. Cette isolation des données contre un accès direct par le programme est appelée masquage des données ou masquage d'informations.

L'abstraction des données fait référence à la fourniture uniquement des informations nécessaires au monde extérieur et au masquage des détails d'implémentation. 

Par exemple, considérons une classe Complex avec des fonctions publiques getReal() et getImag(). Nous pouvons implémenter la classe comme un tableau de taille 2 ou comme deux variables. 

L'avantage de l'abstraction est que nous pouvons changer l'implémentation à tout moment et les utilisateurs de la classe Complex ne seront pas affectés car notre interface de méthode reste la même. Si notre implémentation avait été publique, nous n'aurions pas pu la changer.

### **Héritage :**

L'héritage est le processus par lequel les objets d'une classe acquièrent les propriétés des objets d'une autre classe. Il supporte le concept de classification hiérarchique. 

L'héritage fournit la réutilisabilité. Cela signifie que nous pouvons ajouter des fonctionnalités supplémentaires à une classe existante sans la modifier.

### **Polymorphisme :**

Le polymorphisme fait référence à la capacité de prendre plus d'une forme. Une opération peut exhiber différents comportements dans différentes instances. Le comportement dépend des types de données utilisés dans l'opération.

C++ supporte la surcharge d'opérateurs et la surcharge de fonctions. La surcharge d'opérateurs est le processus qui consiste à faire en sorte qu'un opérateur exhiber différents comportements dans différentes instances. La surcharge de fonctions consiste à utiliser un seul nom de fonction pour effectuer différents types de tâches. Le polymorphisme est largement utilisé dans la mise en œuvre de l'héritage.

### **Liaison Dynamique :**

Dans la liaison dynamique, le code à exécuter en réponse à un appel de fonction est décidé à l'exécution. C++ dispose de fonctions virtuelles pour supporter cela.

### **Passage de Messages :**

Les objets communiquent entre eux en s'envoyant et en recevant des informations. Un message pour un objet est une demande qu'une procédure soit exécutée et donc il invoquera une fonction dans l'objet récepteur qui génère les résultats souhaités. 

Le passage de messages implique de spécifier le nom de l'objet, le nom de la fonction et les informations à envoyer.

## Plus d'informations

[Concepts de Programmation Orientée Objet : Comment passer de Zéro à Un avec les Objets](https://www.freecodecamp.org/news/object-oriented-concepts/)

[Comment Expliquer les Concepts de Programmation Orientée Objet à un Enfant de 6 Ans](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/)